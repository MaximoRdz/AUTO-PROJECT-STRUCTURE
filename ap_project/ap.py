import os

from ap_project.utils import print_tree

class ApProject:
    """ 
    Create a folder with the initial structure of an AP project.
    :param args: Parsed arguments through main.py call
    """
    def __init__(self, args):
        self.output_dir = args.output_dir
        self.packages_list = args.package_names

        if type(self.packages_list) == list:
            for package in self.packages_list:
                self.create_package_structure(package)
        elif type(self.packages_list) == str:
            self.create_package_structure(self.packages_list)

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.output_dir, folder_name)
        if os.path.exists(folder_path):
            print_tree(f"{folder_path} already exists", "folder")
        else:
            os.mkdir(folder_path)
            print_tree(f"{folder_path} created", "folder")

    def create_file(self, filename, extension, folder_path):
        filepath = os.path.join(self.output_dir, folder_path, filename+extension)
        if os.path.exists(filepath):
            print_tree(f"{filepath} already exists", "file")
        else:            
            with open(filepath, "w") as file:
                pass
            print_tree(f"{filepath} created", "file")
    
    def create_package_structure(self, package_name):
        self.create_folder(package_name)
        self.create_file(package_name, ".py", package_name)
        self.create_file("__init__", ".py", package_name)
        self.create_file("constants", ".py", package_name)
        self.create_file("utils", ".py", package_name)
        self.create_file("README", ".md", package_name)
