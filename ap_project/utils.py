import ap_project.constants as ct


def print_tree(message, type):
    """
    Printing format of file/folder creation
    :param message: message to print
    :param type: file or folder printing format
    """
    type_mask = type == "file"
    print("|")
    if type == "file":
        print(f"---- {message}".rjust(ct.FILE_JUST))
    elif type == "folder":
        print("----", message.rjust(ct.FOLDER_JUST))
    else:
        print(message)

    
              
