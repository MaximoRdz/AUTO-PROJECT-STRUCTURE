import os
import json

import structure_gen.constants as ct


def print_tree(message, message_type):
    """
    Printing format of file/folder creation
    :param message: message to print
    :param message_type: file or folder printing format
    """
    type_mask = message_type == "file"

    if message_type == "file":
        print("|----".rjust(ct.FILE_JUST), message)
    elif message_type == "folder":
        print("|")
        print("|----".ljust(ct.FOLDER_JUST), message)
    else:
        print(message)


def read_json(file_path):
    with open(file_path, "r") as file:
        config_data = json.load(file)
    return config_data


def create_config_file(output_dir="./"):
    data = {
        "header": {
            "line 1": "#!/usr/bin/env python",
            "line 2": "__author__ = 'Maximo Rodriguez Herrero'",
            "line 3": "__email__ = 'mxrdhr@gmail.com'"
            },
        "gitignore": [".obsidian", ".venv", ".ipynb_checkpoints", "__pycache__"],
        "package_files": ["__init__.py", "constants.py", "utils.py", "README.md"]
    }
    json_object = json.dumps(data)
    with open("../config.json", "w") as file:
        file.write(json_object)







