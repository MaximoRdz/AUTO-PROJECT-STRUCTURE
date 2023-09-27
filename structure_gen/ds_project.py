import os

from structure_gen.structure_gen import StructureGen


class DsProject(StructureGen):
    """
    StructureGen child class that creates a specific workplace structure recurrently used for
    DataScience projects.
    """

    def __init__(self, project_type, output_dir, packages, folders):
        super().__init__(project_type, output_dir, packages, folders)

    def create_workplace(self):
        """
        The dev project structure consist of:
        ├── DS Project
        │   ├── images/
        │   ├── test/
        │   ├── data/
        │   ├── notebooks/
        │   ├── reports/
        │   ├── models/
        │   │   ├── __init__.py
        │   │   ├── constants.py
        │   │   ├── utils.py
        │   │   ├── model.py
        │   │   └── README.md
        │   ├── .gitignore
        │   ├── config.json
        │   ├── main.py
        │   └── README.md
        └──
        :return:
        """
        self.create_file(os.path.join(self.output_dir, "main.py"), self.header)
        self.create_file(os.path.join(self.output_dir, "README.md"), None)
        self.create_file(os.path.join(self.output_dir, ".gitignore"), self.gitignore)

        self.create_folder("data")
        self.create_folder("notebooks")
        self.create_folder("reports")

        self.create_package("models")

        for package in self.packages:
            if package == "default":
                continue
            self.create_package(package)

        for folder in self.folders:
            self.create_folder(folder)
