import argparse

from ap_project.ap import ApProject

parser = argparse.ArgumentParser(description="Automatic Project Structure Generator")

parser.add_argument("--type", required=True, choices=["AP", "DS"], 
                    type=str, help="Project struture type, AP: Apps or APIs; DS: Data Science")
parser.add_argument("--output_dir", required=True, 
                    type=str, help="Workplace output directory")
parser.add_argument("--package_names", required=False, default="default", 
                    nargs="*", type=str, help="Packages name to be created")
parser.add_argument("--folders", required=False, 
                    type=str, help="create empty folders")



if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    if args.type == "AP":
        project_structure = ApProject(args)
        #project_structure.create()
    else:
        print("launch DS")
    
    



