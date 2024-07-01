import json
import csv
import re


offsets = {}

with open("./utils/legacy-files/1.csv", encoding="utf-8") as f:
    data = csv.reader(f, delimiter=",")
    
    offsets = {row[0]: row[1] for row in data if row[0] != "id"}

with open("./utils/legacy-files/2.py", encoding="utf-8") as f:
    result = re.findall(r"read_offsets_([0-9]*)\(\)\:\n\s*offsets = '(.*)'", f.read())

    for group in result:
        if group[0] in offsets:
            print("Found duplicate: ", group[0])
            continue

        offsets.update({group[0]: group[1]})


if len(offsets) != 71:
    print(f"Only {len(offsets)} offsets found; expecting 71!")

else:
    print(f"All {len(offsets)} offsets should have been parsed!")



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
            print("Found duplicate: ", group[1])
            continue

        version_numbering.update({
            numeric: {
                "full": group[1],
                "short": group[0],
                "numeric": numeric
            }
        })

if len(version_numbering) != 71:
    print(f"Only {len(version_numbering)} version numberings found; expecting 71!")

else:
    print(f"All {len(version_numbering)} version numberings should have been parsed!")


print("Offsets: ", json.dumps(list(offsets.keys())))
print("Version Numberings: ", json.dumps(list(version_numbering.keys())))



# Use order of discord messages
for numeric_version in version_numbering:
    offsets_loaded = json.loads(offsets[str(numeric_version)])

    new_offsets = {
        "fov": {
            "available": offsets_loaded["0"]["a"],
            "offsets": offsets_loaded["0"]["o"]
        },
        "hide-hand": {
            "available": offsets_loaded["1"]["a"],
            "offsets": offsets_loaded["1"]["o"]
        },
        "sensitivity": {
            "available": offsets_loaded["2"]["a"],
            "offsets": offsets_loaded["2"]["o"]
        }
    }
    if offsets_loaded["3"]["a"]:
        new_offsets.update({
            "server-domain": {
                "available": offsets_loaded["3"]["a"],
                "offsets": offsets_loaded["3"]["o"][0]
            }
        })
        new_offsets.update({
            "server-port": {
                "available": offsets_loaded["3"]["a"],
                "offsets": offsets_loaded["3"]["o"][1]
            }
        })

        # Auto trim
        if new_offsets["server-domain"]["offsets"][-1] == 0:
            print(f"{numeric_version} has an invalid zero offset for the server pointer! Removing it...")
            new_offsets["server-domain"]["offsets"].pop(-1)

    else:
        new_offsets.update({
            "server-domain": {
                "available": offsets_loaded["3"]["a"],
                "offsets": []
            }
        })
        new_offsets.update({
            "server-port": {
                "available": offsets_loaded["3"]["a"],
                "offsets": []
            }
        })

    data = {
        "version": version_numbering[numeric_version],
        "release-date": None,
        "pointers": new_offsets,
    }

    with open(f"versions/{data['version']['full']}.json", "w") as f:
        json.dump(data, f, indent=4)




