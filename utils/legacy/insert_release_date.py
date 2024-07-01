"""

    Inserts release dates created from 'get_release_dates.py' (stored in 'release-dates.json') into all version data

    Attention: Overrides all

"""

import json
import datetime


release_dates = {}

with open("./utils/legacy/release-dates.json") as f:
    release_dates = json.load(f)

# Override version data
for version_full, release_date in release_dates.items():
    version_data = {}
    
    # Get old version data
    with open(f"./versions/{version_full}.json") as f:
        version_data = json.load(f)

    if version_data["version"]["full"] != version_full:
        print(f"[!] Mismatching full version string ({version_full=}, {version_data['version']['full']=})")

    # Insertion
    version_data["release-date"] = release_date

    # Write new version data
    with open(f"./versions/{version_full}.json", "w") as f:
        json.dump(version_data, f, indent=4)
