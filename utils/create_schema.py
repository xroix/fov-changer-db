import json

from pydantic import BaseModel, Field, PastDatetime, PositiveInt, model_validator


JSON_SCHEMA_FILE = "version.schema.json"


class Version(BaseModel):
    """ A game version can be specified in a number of ways."""
    full: str = Field(pattern=r'^[0-9.]*$')
    short: str = Field(pattern=r'^[0-9.]*$')
    numeric: int = Field(gt=0)

    @model_validator(mode="after")
    def check_numeric(self):
        assert int(self.full.replace(".", "")) == self.numeric, "The full version string, when stripped of dots, must match the numeric version."
        return self

class Pointer(BaseModel):
    """ Describing one version specific pointer needed by FOV-Changer."""
    available: bool
    offsets: list[int]

    @model_validator(mode="after")
    def check_offsets(self):
        assert self.available or not self.offsets, "Offsets should be provided when pointer is available."
        return self

class Pointers(BaseModel):
    """ Holding all needed pointers for a specific version """
    fov: Pointer
    hide_hand: Pointer = Field(alias="hide-hand")
    sensitivity: Pointer
    server_domain: Pointer = Field(alias="server-domain")
    server_port: Pointer = Field(alias="server-port")

class VersionData(BaseModel):
    """ Models the data needed by FOV-Changer for a specific version."""
    version: Version = Field()
    release_date: PositiveInt = Field(alias="release-date")
    pointers: Pointers

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "version": {
                        "full": "1.16.2.0",
                        "short": "1.16.0",
                        "numeric": 11620
                    },
                    "release-date": 1592863200,
                    "pointers": {
                        "fov": {
                            "available": True,
                            "offsets": [
                                59104712,
                                192,
                                2280,
                                176,
                                288,
                                240
                            ]
                        },
                        "hide-hand": {
                            "available": True,
                            "offsets": [
                                59332344,
                                192,
                                3400,
                                176,
                                0,
                                3304,
                                232
                            ]
                        },
                        "sensitivity": {
                            "available": True,
                            "offsets": [
                                59332344,
                                200,
                                2016,
                                176,
                                3152,
                                264,
                                64,
                                20
                            ]
                        },
                        "server-domain": {
                            "available": False,
                            "offsets": []
                        },
                        "server-port": {
                            "available": False,
                            "offsets": []
                        }
                    }
                }
            ]
        }
    }


if __name__ == "__main__":
    with open(JSON_SCHEMA_FILE, "w") as f:
        json.dump(VersionData.model_json_schema(by_alias=True), f, indent=4)

    print("[*] Finished")
