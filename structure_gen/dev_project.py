import os.path

from structure_gen.structure_gen import StructureGen


class DevProject(StructureGen):
    """
    StructureGen child class that creates a specific workplace structure recurrently used for
    dev projects.
    """

    def __init__(self, project_type, output_dir, packages, folders):
        super().__init__(project_type, output_dir, packages, folders)
        self.create_workplace()

    def create_workplace(self):
        """
        The dev project structure consist of:
        ├── AP Project
        │   ├── images/
        │   ├── test/
        │   ├── Package Name
        │   │   ├── __init.py__
        │   │   ├── constants.py
        │   │   ├── utils.py
        │   │   ├── package_name.py
        │   │   └── README.md
        │   ├── .gitignore
        │   ├── main.py
        │   └── README.md
        └──
        :return:
        """
        self.create_folder("")
        self.create_file(os.path.join(self.output_dir, "main.py"), self.header)
        self.create_file(os.path.join(self.output_dir, "README.md"), None)
        # self.create_file(".config", self.header)

        for package in self.packages:
            self.create_package(package)

        for folder in self.folders:
            self.create_folder(folder)
