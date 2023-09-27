import os

from structure_gen.structure_gen import StructureGen


class DevProject(StructureGen):
    """
    StructureGen child class that creates a specific workplace structure recurrently used for
    dev projects.
    """

    def __init__(self, project_type, output_dir, packages, folders):
        super().__init__(project_type, output_dir, packages, folders)

    def create_workplace(self):
        """
        The dev project structure consist of:
        ├── DEV Project
        │   ├── images/
        │   ├── test/
        │   ├── Package Name
        │   │   ├── __init__.py
        │   │   ├── constants.py
        │   │   ├── utils.py
        │   │   ├── package_name.py
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

        for package in self.packages:
            self.create_package(package)

        for folder in self.folders:
            self.create_folder(folder)
