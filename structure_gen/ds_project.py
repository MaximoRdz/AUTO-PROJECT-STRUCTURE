import os.path

from structure_gen.structure_gen import StructureGen


class DsProject(StructureGen):
    """
    StructureGen child class that creates a specific workplace structure recurrently used for
    data science projects.
    """

    def __init__(self, project_type, output_dir, packages, folders):
        super().__init__(project_type, output_dir, packages, folders)

    def create_workplace(self):
        """
        The DS project structure consist of:
        ├── DS Project
        │   ├── images/
        │   ├── data/
        │   ├── notebooks/
        │	├── model/
        │	│   ├── __init__.py
        │	│   ├── constants.py
        │	│   ├── utils.py
        │	│   ├── model.py
        │   │   ├── visualization.py
        │	│   └── README.md
        │   ├── .gitignore
        │   ├── config.json
        │   ├── main.py
        └── └── README.md
        :return:
        """
        self.create_file(os.path.join(self.output_dir, "main.py"), self.header)
        self.create_file(os.path.join(self.output_dir, "README.md"), None)
        self.create_file(os.path.join(self.output_dir, ".gitignore"), self.gitignore)

        for package in self.packages:
            if package is None:
                continue
            self.create_package(package)
        
        # ADD extra files in DS package /model/
        self.create_file(os.path.join(self.output_dir, "model", "visualization.py"), self.header)

        for folder in self.folders:
            if folder is None:
                continue
            self.create_folder(folder)
