"""

    Converts old SQL database and FastAPI server into a newer and consistent format

    Attention: Override existing version.json files!!!

"""

import json
import csv
import re


VERSION_COUNT = 71


########################
# 1. Parse old backups #
########################

pointers = {}

with open("./utils/legacy-files/1.csv", encoding="utf-8") as f:
    data = csv.reader(f, delimiter=",")
    
    pointers = {
        row[0]: json.loads(row[1]) for row in data 
        if row[0] != "id"
    }

with open("./utils/legacy-files/2.py", encoding="utf-8") as f:
    result = re.findall(r"read_offsets_([0-9]*)\(\)\:\n\s*offsets = '(.*)'", f.read())

    for group in result:
        if group[0] in pointers:
            print(f"[!] Found duplicate pointer, ignoring it: {group[0]}")
            continue

        pointers.update({
            group[0]: json.loads(group[1])
        })


if len(pointers) != VERSION_COUNT:
    print(f"[!] Only {len(pointers)} pointers found; expecting {VERSION_COUNT}!")

else:
    print(f"[*] All {VERSION_COUNT} pointers were parsed.")


##################################################################
# 2. Check #mc-versions discord channel for full version numbers #
##################################################################

# "full" == internal version of the Windows edition
version_numbering = {
    11460050: {"full": "1.14.6005.0", "short": "1.14.60 ", "numeric": 11460050},
    11620: {"full": "1.16.2.0", "short": "1.16.0", "numeric": 11620},
    1161020: {"full": "1.16.102.0", "short": "1.16.1", "numeric": 1161020},
    11610020: {"full": "1.16.1002.0", "short": "1.16.10", "numeric": 11610020},
}

with open("./utils/legacy-files/dc-messages.txt", encoding="utf-8") as f:
    result = re.findall(r"❯\s*([0-9.]*)\s*\(([0-9.]*)\)", f.read())

    for group in result:
        numeric = int(group[1].replace(".",""))

        if numeric in version_numbering:
            print("[!] Found duplicate version numbering: ", group[1])
            continue

        version_numbering.update({
            numeric: {
                "full": group[1],
                "short": group[0],
                "numeric": numeric
            }
        })

if len(version_numbering) != VERSION_COUNT:
    print(f"[!] Only {len(version_numbering)} version numberings found; expecting {VERSION_COUNT}!")

else:
    print(f"[*] All {VERSION_COUNT} version numberings were parsed.")

# print("Offsets: ", json.dumps(list(pointers.keys())))
# print("Version Numberings: ", json.dumps(list(version_numbering.keys())))


######################################
# 3. Generate new version.json files #
######################################

# Use the order of the discord messages
for numeric_version in version_numbering:
    version_pointers = pointers[str(numeric_version)]

    new_pointers = {
        "fov": {
            "available": version_pointers["0"]["a"],
            "offsets": version_pointers["0"]["o"]
        },
        "hide-hand": {
            "available": version_pointers["1"]["a"],
            "offsets": version_pointers["1"]["o"]
        },
        "sensitivity": {
            "available": version_pointers["2"]["a"],
            "offsets": version_pointers["2"]["o"]
        }
    }
    if version_pointers["3"]["a"]:
        new_pointers.update({
            "server-domain": {
                "available": version_pointers["3"]["a"],
                "offsets": version_pointers["3"]["o"][0]
            },
            "server-port": {
                "available": version_pointers["3"]["a"],
                "offsets": version_pointers["3"]["o"][1]
            }
        })

    else:
        new_pointers.update({
            "server-domain": {
                "available": version_pointers["3"]["a"],
                "offsets": []
            },
            "server-port": {
                "available": version_pointers["3"]["a"],
                "offsets": []
            }
        })    

    # Auto trim
    if new_pointers["server-domain"]["available"] and new_pointers["server-domain"]["offsets"][-1] == 0:
        print(f"\t[!] {numeric_version} has an invalid zero offset for the server pointer! Removing it...")
        new_pointers["server-domain"]["offsets"].pop(-1)

    data = {
        "version": version_numbering[numeric_version],
        "release-date": None,
        "pointers": new_pointers,
    }

    with open(f"versions/{data['version']['full']}.json", "w") as f:
        json.dump(data, f, indent=4)

print("[*] All version.json were created.")


