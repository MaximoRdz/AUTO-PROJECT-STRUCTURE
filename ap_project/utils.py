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

    


              
create_config_file()