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


def create_folder(folder_name, folder_path):
    """Creates a folder in the specify path"""
    complete_path = os.path.join(folder_path, folder_name)
    if os.path.exists(complete_path):
        print_tree(f"{complete_path} already exists", "folder")
    else:
        os.mkdir(complete_path)


def create_file(file_name, extension, file_path, header=None):
    """
    Creates an empty file unless otherwise specify
    :param header: if True a header is added to the file, default False
    """
    complete_path = os.path.join(file_path, file_name + extension)
    if os.path.exists(complete_path):
        print_tree(f"{complete_path} already exists", "file")
    else:
        with open(complete_path, "w") as file:
            if header is None:
                pass
            else:
                file.writelines(header)
        print_tree(f"{complete_path} created", "file")




