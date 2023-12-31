import os

import structure_gen.constants as ct
from structure_gen.utils import print_tree, read_json, create_config_file


class StructureGen:
    """ 
    Parent class capable of parsing main.py args and creating the project
    structure.
    :param project_type: "DEV" for dev projects "DS" for Data Science projects.
    :param output_dir: Path to locate the workplace, str.
    :param packages: List of packages to create, list(str).
    :param folders: List of emtpy folders to create, list(str).
    """
    def __init__(self, project_type, output_dir, packages, folders):
        self.project_type = project_type
        self.output_dir = output_dir
        self.packages = packages
        self.folders = folders

        try:
            self.config_info = read_json(ct.CONFIG_FILE_PATH)
        except FileNotFoundError:
            create_config_file()
            self.config_info = read_json(ct.CONFIG_FILE_PATH)

        self.header = "\n".join(list(self.config_info["header"].values()))
        self.gitignore = ct.GITIGNORE_LINE_SEP.join(self.config_info["gitignore"])

        self.create_folder("")    # Create workplace folder

    @staticmethod
    def create_file(file_path, file_content=None):
        """
        Creates an empty file unless otherwise specify
        :param file_path: Complete path to file including extension C//...//name.ext
        :param file_content: Write in file if not None
        """
        if os.path.exists(file_path):
            print_tree(f"{file_path} already exists", "file")
        else:
            with open(file_path, "w") as file:
                if file_content is None:
                    pass
                else:
                    file.writelines(file_content)
            print_tree(f"{file_path} created", "file")

    def create_folder(self, folder_name):
        """Creates a folder in the specify path"""
        complete_path = os.path.join(self.output_dir, folder_name)
        if os.path.exists(complete_path):
            print_tree(f"{complete_path} already exists", "folder")
        else:
            os.mkdir(complete_path)
            print_tree(f"{complete_path} created", "folder")

    def create_package(self, package_name):
        """
        Create a folder with python's module structure
        package: __init__.py, utils.py, constants.py, README.md and package.py
        """
        self.create_folder(package_name)
        package_path = os.path.join(self.output_dir, package_name)
        package_files = self.config_info["package_files"].copy()
        package_files.extend([f"{package_name}.py"])

        for file in package_files:
            file_path = os.path.join(package_path, file)
            if ".md" in file:
                self.create_file(file_path, None)
            else: 
                self.create_file(file_path, self.header)



   
        

    


