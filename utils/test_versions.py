import json
import os
import glob

import pytest

from create_schema import VersionData, Pointer, Pointers, Version


def pytest_generate_tests(metafunc: pytest.Metafunc):
    """ Run tests for every version data file in ./versions
        https://stackoverflow.com/a/63212783
    """
    file_list = glob.glob("./versions/*.json")
    metafunc.parametrize("file_name", file_list)


@pytest.fixture(autouse=True)
def seen_versions():
    """ For checking whether versions are unique
    """
    return {
        "full": [], "short": [], "numeric": []
    }


def test_version_data(file_name, seen_versions):
    """ Runt test on a specific version data file
    """
    text = None
    
    with open(file_name) as f:
        text = f.read()

    assert text, "File was empty"

    version_data = VersionData.model_validate_json(text, strict=True)

    # Some extra validation
    assert version_data.version.full not in seen_versions["full"], f"'full' version '{version_data.version.full}' already exists"
    seen_versions["full"].append(version_data.version.full)

    assert version_data.version.short not in seen_versions["short"], f"'short' version '{version_data.version.short}' already exists"
    seen_versions["short"].append(version_data.version.short)

    assert version_data.version.numeric not in seen_versions["numeric"], f"'numeric' version '{version_data.version.numeric}' already exists"
    seen_versions["numeric"].append(version_data.version.numeric)
        
        # print("\t" + str(e).replace("\n", "\n\t"))
