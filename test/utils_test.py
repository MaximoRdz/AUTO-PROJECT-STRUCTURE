import json
import pytest

from structure_gen.utils import read_json, create_config_file

"""
To test read_json it is necessary to create a set up where we first create a json
we know and save it on a file to then retrieve it with read_json and assert that 
they are both the same. 
TDD:
Test scenarios:
    - wrong extension
    - not found .json
"""


@pytest.fixture()
def my_json(tmp_path):
    test_dict = {"Name": "Maximo",
                 "Last Name": "Rodriguez",
                 "Phone": "999999999",
                 "Family": {"Mother": 1,
                            "Father": 1,
                            "Brothers": 0,
                            "Sisters": 1
                            }
                 }
    with open(tmp_path / "my_json.json", "w") as json_file:
        json.dump(test_dict, json_file)

    return test_dict


def test_read_json(my_json, tmp_path):
    assert read_json(tmp_path / "my_json.json") == my_json


def test_read_json_not_found():
    with pytest.raises(FileNotFoundError):
        read_json("notfound.json")


def test_read_json_extension(tmp_path):
    with open(tmp_path / "no_json.txt", "w") as file:
        file.write("Hello World!")

    with pytest.raises(json.decoder.JSONDecodeError):
        read_json(tmp_path / "no_json.txt")


"""
We can use the tested read_json to also test create_config_file
"""


def test_create_config_file(tmp_path):
    data = {
        "header": {
            "line 1": "#!/usr/bin/env python",
            "line 2": "__author__ = 'Maximo Rodriguez Herrero'",
            "line 3": "__email__ = 'mxrdhr@gmail.com'"
            },
        "gitignore": [".obsidian", ".venv", ".ipynb_checkpoints", ".idea", "__pycache__/", ".pytest_cache/"],
        "package_files": ["__init__.py", "constants.py", "utils.py", "README.md"]
    }
    create_config_file(tmp_path)
    assert data == read_json(tmp_path / "config.json")
