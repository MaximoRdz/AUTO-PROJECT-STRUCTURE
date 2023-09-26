## Program Design
![Program Design](https://github.com/MaximoRdz/AUTO-PROJECT-STRUCTURE/blob/main/images/program_design.PNG)
## Config File
Generate default config file with `create_config_file()` function [`utils.py`](https://github.com/MaximoRdz/AUTO-PROJECT-STRUCTURE/blob/main/structure_gen/utils.py) 
```json
{
    "gitignore": [
        ".obsidian",
        ".venv",
        ".ipynb_checkpoints",
        ".idea",
        "__pycache__/"
    ],
    "header": {
        "line 1": "#!/usr/bin/env python",
        "line 2": "__author__ = 'Maximo Rodriguez Herrero'",
        "line 3": "__email__ = 'mxrdhr@gmail.com'"
    },
    "package_files": [
        "__init__.py",
        "constants.py",
        "utils.py",
        "README.md"
    ]
}
```
## DEV Project
### Functionality
- Create as many packages as needed each of them formed by `__init__.py`, `constants.py`, `utils.py`, `package_name.py` and `README.md`.
- For every script is possible to add a header inside the config file similar to
```python
__author__ = "Maximo Rodriguez Herrero"
__copyright__ = "Copyright 2007"
__credits__ = ["Guido van Rossum"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Maximo Rodriguez"
__email__ = "mxrdhr@gmail.com"
__status__ = "Production"
```
introducing the information in the `config.json` file.
- Create as many empty folder as needed, by default `.\test\` and `.\images` are created.
- Predetermined `.gitignore` will be created any extra to-be-ignored files can be also specify in `config.json`.
