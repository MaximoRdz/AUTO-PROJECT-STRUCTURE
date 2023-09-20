import json
import constants as ct


def print_tree(message, type):
    """
    Printing format of file/folder creation
    :param message: message to print
    :param type: file or folder printing format
    """
    type_mask = type == "file"
    
    if type == "file":
        print("|----".rjust(ct.FILE_JUST), message)
    elif type == "folder":
        print("|")
        print("|----".ljust(ct.FOLDER_JUST), message)
    else:
        print(message)

    
def create_config_file(output_dir="./"):
    data = {    
        "header":{
                "__author__": "Máximo Rodríguez Herrero", 
                "__email__": "mxrdhr@gmail.com"
            }, 
        "folders":["test", "images"], 
        "gitignore": [".obsidian", ".venv"], 
        "package_files": ["__init__.py", "constants.py", "utils.py", "README.md"]
    }


    json_object = json.dumps(data)
    with open("config.json", "w") as file:
        file.write(json_object)

              
create_config_file()