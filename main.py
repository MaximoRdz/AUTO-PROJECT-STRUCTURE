import argparse

from ap_project.ap import ApProject
from structure_gen.structure_gen import StructureGen

parser = argparse.ArgumentParser(description="Automatic Project Structure Generator")

parser.add_argument("--type", required=True, choices=["AP", "DS"], 
                    type=str, help="Project struture type, AP: Apps or APIs; DS: Data Science")
parser.add_argument("--output_dir", required=True, 
                    type=str, help="Workplace output directory")
parser.add_argument("--packages", required=False, default=["default"], 
                    nargs="*", type=str, help="Packages to be created")
parser.add_argument("--folders", required=False, default=["test", "images"], 
                    nargs="*", type=str, help="create empty folders")



if __name__ == "__main__":
    # Parse and asign the arguments
    args = parser.parse_args()
    project_type = args.type()
    output_dir = args.output_dir()
    packages = args.packages()
    folders = args.folders()

    if project_type == "AP":
        project_structure = StructureGen(project_type,output_dir, packages, folders)
    else:
        print("launch DS")
    
    



