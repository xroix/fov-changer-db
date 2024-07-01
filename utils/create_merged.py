import json
import os


MERGED_FILE = "versions.merged.json"

combined = []

for file in os.listdir("./versions/"):
    filename = os.fsdecode(file)
    data = None

    try:
        with open(f"./versions/{filename}") as f:
            data = json.load(f)

    except Exception as e:
        print(f"[!] '{filename}' Invalid JSON. (Error: '{e}')")
        continue
    
    # combined.update({
    #     data["version"]["full"]: {
    #         "v": {
    #             "f": data["version"]["full"],
    #             "s": data["version"]["short"],
    #             "n": data["version"]["numeric"]
    #         }
    #     }
    # })
    combined.append(data)

with open(MERGED_FILE, "w") as f:
    json.dump(combined, f)