import argparse

import structure_gen.constants as ct
from structure_gen.dev_project import DevProject
from structure_gen.ds_project import DsProject
from structure_gen.utils import create_config_file


parser = argparse.ArgumentParser(description="Automatic Project Structure Generator")

parser.add_argument("--type", required=True, choices=["DEV", "DS"],
                    type=str, help="Project structure type, DEV: Apps or APIs; DS: Data Science")
parser.add_argument("--output_dir", required=True, 
                    type=str, help="Workplace output directory")
parser.add_argument("--packages", required=False, default=None, 
                    nargs="*", type=str, help="Packages to be created")
parser.add_argument("--folders", required=False, default=None, 
                    nargs="*", type=str, help="create empty folders")
parser.add_argument("--config", type=bool, required=False, 
                    default=False, help="Input Config True if to create the config file")


if __name__ == "__main__":
    # Parse and assign the arguments
    args = parser.parse_args()

    if args.config:
        create_config_file()

    project_type = args.type
    output_dir = args.output_dir

    # Default project packages extended with user required folders (if any)
    if args.packages is None:
        packages = ct.PROJECT_INFO[project_type]["packages"]
    else:
        packages = ct.PROJECT_INFO[project_type]["packages"].extend(args.packages)

    # Default project folders extended with user required folders (if any)
    if args.folders is None:
        folders = ct.PROJECT_INFO[project_type]["folders"]
    else:
        folders = ct.PROJECT_INFO[project_type]["folders"].extend(args.folders)
    print(packages)
"""    if project_type == "DEV":
        project_structure = DevProject(project_type, output_dir, packages, folders).create_workplace()
    else:
        project_structure = DsProject(project_type, output_dir, packages, folders).create_workplace()"""
    
    



