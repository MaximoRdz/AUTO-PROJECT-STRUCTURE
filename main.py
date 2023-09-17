import argparse

from ap_project.ap import ApProject

parser = argparse.ArgumentParser(description="Automatic Project Structure Generator")

parser.add_argument("--type", required=True, choices=["AP", "DS"], 
                    type=str, help="Project struture type, AP: Apps or APIs; DS: Data Science")
parser.add_argument("--output_dir", required=True, 
                    type=str, help="Workplace output directory")

parser.add_argument("--package_name", required=False, default="default", 
                    nargs="*", type=str, help="Packages name to be created")






if __name__ == "__main__":
    args = parser.parse_args()
    print(args.package_name)
    if args.type == "AP":
        ApProject()
    else:
        print("launch DS")
    
    



