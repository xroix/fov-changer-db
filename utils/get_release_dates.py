import re
import os
import time
import random
import requests
import json
import datetime



all_release_dates = {}

for file in os.listdir("./versions/"):
    filename = os.fsdecode(file)

    version_data = None

    try:
        with open(f"./versions/{filename}") as f:
            version_data = json.load(f)

    except Exception as e:
        print(f"[!] '{filename}' Invalid JSON. (Error: '{e}')")
        continue

    # Retrieve release date information from minecraft.wiki
    response = requests.get(f"https://minecraft.wiki/w/Bedrock_Edition_{version_data['version']['short']}")
    
    release_date = re.findall(r'"field":\s*"([A-Za-z,0-9\s]*)",\s*"label":\s*"Release date"', response.text)
    release_date2 = re.findall(r'<b>[a-zA-Z,0-9\s]*Windows[a-zA-Z,0-9\s]*<\/b>: ([0-9,a-zA-Z\s]{3,})', response.text)
    full_version = re.findall(r'<b>[a-zA-Z,0-9\s]*Windows[a-zA-Z,0-9\s]*<\/b>: ([0-9.]*)<br', response.text)

    print(f"[{version_data['version']['full']}] {release_date=} {release_date2=} {full_version=}")

    if not release_date and not release_date2:
        print(f"\t[!] No release date found")
    else:
        release_date = release_date[0] if release_date else release_date2[0]
        release_date = release_date.strip()
    
    if not full_version:
        print(f"\t[!] No full version found")
    else:
        full_version = full_version[0].strip()

    if full_version and full_version != version_data['version']['full']:
        print("\t[!] Unexpected full version provided") 

    try:
        release_date_unix = int(datetime.datetime.strptime(release_date, "%B %d, %Y").timestamp())

    except ValueError and TypeError:
        print("\t[!] Unable to convert to an unix timestamp")
        release_date_unix = 0

    all_release_dates.update({
        version_data['version']['full']: release_date_unix
    })

    time.sleep(1 + 1 * random.random())

#    break

with open("./utils/release-dates.json", "w") as f:
    json.dump(all_release_dates, f, indent=4)

print("[*] Finished")
