"""

    Fixes the invalid release dates of versions, mainly:

     - 1.14.6005.0 until 1.21.4101.0 were UTC+2
     - 1.21.4301.0 until 1.21.6201.0 were UTC+1

     Henceforth, all timestamps must assume UTC+0.

"""

import pathlib
import json
import datetime
import zoneinfo

found_12141010 = False

for path in pathlib.Path("./versions/").iterdir():  # Assumes an alphabetically sorted directory !!!!
    if not path.is_file():
        continue

    with open(path, "r") as file:
        data = json.load(file)

    # Check full version
    full_version = data["version"]["full"]

    print(f" * Fixing '{full_version}'")

    if full_version  == "1.21.4301.0":
        found_12141010 = True

    # Fixing timestamp
    if not found_12141010:
        delta = datetime.timedelta(hours=2)
    else:
        delta = datetime.timedelta(hours=1)

    to_timezone = zoneinfo.ZoneInfo("UTC")
    from_timezone = datetime.timezone(delta)

    timestamp = datetime.datetime.fromtimestamp(data["release-date"], tz=from_timezone)
    fixed_timestamp = datetime.datetime(year=timestamp.year, month=timestamp.month, day=timestamp.day, tzinfo=to_timezone)

    print(f"\t{timestamp.timestamp()} -> {fixed_timestamp.timestamp()}")
    print(f"\t{timestamp.strftime('%d/%m/%Y, %H:%M:%S')} -> {fixed_timestamp.strftime('%d/%m/%Y, %H:%M:%S')}")

    # Write changes
    data["release-date"] = int(fixed_timestamp.timestamp())

    with open(path, "w") as file:
        json.dump(data, file, indent=4)
        pass

print("Finished")
