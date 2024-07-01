import json
import os
import datetime



seen_full_versions = []
seen_short_versions = []
seen_numeric_versions = []


for file in os.listdir("./versions/"):
    filename = os.fsdecode(file)
    data = None

    try:
        with open(f"./versions/{filename}") as f:
            data = json.load(f)

    except Exception as e:
        print(f"[!] '{filename}' Invalid JSON. (Error: '{e}')")
        continue

    print(f"[*] {filename}")
    
    try:
        assert "version" in data, "Missing 'version'."
        assert "full" in data["version"], "Missing 'full'."
        assert "short" in data["version"], "Missing 'short'."
        assert "numeric" in data["version"], "Missing 'numeric'."

        assert int(data["version"]["full"].replace(".", "")) == data["version"]["numeric"], "'full' does not match 'numeric'."

        assert data["version"]["full"] not in seen_full_versions, f"'full' version '{data['version']['full']}' already exists"
        assert data["version"]["short"] not in seen_short_versions, f"'short' version '{data['version']['short']}' already exists"
        assert data["version"]["numeric"] not in seen_numeric_versions, f"'numeric' version '{data['version']['numeric']}' already exists"

        assert "release-date" in data, "Missing 'release-date'."
        assert data["release-date"], "'release-date' is 0"
        assert datetime.datetime.fromtimestamp(data["release-date"]).year >= 2020, f"'release-date' is too old"

        assert "pointers" in data, "Missing 'pointers'."
        assert "fov" in data["pointers"], "Missing 'fov'."
        assert "hide-hand" in data["pointers"], "Missing 'hide-hand'."
        assert "sensitivity" in data["pointers"], "Missing 'sensitivity'."
        assert "server-domain" in data["pointers"], "Missing 'server-domain'."
        assert "server-port" in data["pointers"], "Missing 'server-port'."

        for name, info in data["pointers"].items():
            assert "available" in info, f"{name} is missing 'available'."
            assert "offsets" in info, f"{name} is missing 'offsets'."

            if info["available"]:
                assert len(info["offsets"]) != 0, f"{name} is available but has no offsets."
            else:
                assert len(info["offsets"]) == 0, f"{name} is not available but has offsets."
           

    except AssertionError as e:
        print(f"\t[!] '{filename}' Failed test: '{e}'")

    except ValueError and TypeError as e:
        print(f"\t[!] '{filename}' Failed test, encountered error: '{e}'")
