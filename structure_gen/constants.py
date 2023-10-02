import os

FILE_JUST = 10    # Justify string for files tree_print()
FOLDER_JUST = 5    # Justify string for folders tree_print()
CONFIG_FILE_PATH = os.path.join(".", "config.json")
GITIGNORE_LINE_SEP = "".join(["\n", "# ", 20*"-", "\n"])
PROJECT_INFO = {
    "DEV": {
        "folders": ["images", "test"],
        "packages": ["default"]
    },
    "DS": {
        "folders": ["images", "data", "notebooks"],
        "packages": ["model"]
    }
}

