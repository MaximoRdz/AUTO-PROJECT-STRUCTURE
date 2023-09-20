import os
import json




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



def create_folder(folder_name, folder_path):
    """Creates a folder in the specify path"""
    complete_path = os.path.join(folder_path, folder_name)
    if os.path.exists(complete_path):
        print_tree(f"{complete_path} already exists", "folder")
    else:
        os.mkdir(complete_path)





