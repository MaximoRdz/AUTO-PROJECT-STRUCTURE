# Automatic Project Structure Generator
## Project Overview
Every coding project has unique goals, different requirements and specific features that are not shared across field-related projects. However, if I have learned anything about computer science is that organization and structure consistency is key to success, that is why this repo is focused on developing an automatic initial workplace so that the structure and initial steps of every project remain consistent. Due to my specialization, there are two main branches of projects that I work on in a day to day fashion: developing **APPs**, **API**, . . .; or, what I call, **DEV** projects and Data Science (**DS**) projects.
## Quick Start
Use this repository to initialize your workplaces for Developing or Data Science, 
```bash
git clone https://github.com/MaximoRdz/AUTO-PROJECT-STRUCTURE.git
cd AUTO-PROJECT-STRUCTURE
```
Run `main.py` on the terminal specifying your necessities, 
```cmd
python main.py --type DS --output_dir ./example --packages run_model train_model 
```
This example would produce the following structure
==add tree structure==
For further customization check the documentation.
## Shared Items
Despite the differences between projects there are always some commonalities.
- `.gitignore`: Avoid git control over certain files like `.ipynb_checkpoints/`, `.obsidian`, etc.
- `./images/`: Images used on the readmes.
- `./test/`: Used to storage tests of API, APP, models, . . . 
- `config.json`: Includes the configurable information of the automatized process.
	- `header`: Lines to write at the beginning of `.py` files.
	- `gitignore:` File extensions or folders to be ignore on git.
	- `package_files`: Desired structure of our customized python packages.
## DEV Projects
DEV projects consist on the `main.py` file located in the project folder and surrounded by packages that feed to `main.py` the necessary tools to work properly. Every package has associated both `constants.py` and `utils.py` files which I find necessary to provide support to `package.py`, and, of course a `README.md` that further explains the package functionality.
### DEV Example Structure
```bash
├── DEV Project  
│   ├── images/
│   ├── test/ 
│   ├── PackageName/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── utils.py
│   │   ├── package_name.py
│   │   └── README.md
│   ├── .gitignore
│   ├── config.json
│   ├── main.py
│   └── README.md
└── 
```

## DS Projects
Data Science projects generally consist of exploratory notebooks, models (including train and run) and visualization tools
```bash
├── DS Project  
│   ├── images/
│   ├── data/ 
│   ├── notebooks/  
│   │	├── models/
│   │	│   ├── __init__.py
│   │	│   ├── constants.py
│   │	│   ├── utils.py
│   │	│   ├── model.py
│   │   │   ├── visualization.py
│   │	└── └── README.md
│   ├── .gitignore
│   ├── config.json
│   ├── main.py
└── └── README.md
```
TODO
- [Home - Cookiecutter Data Science (drivendata.github.io)](http://drivendata.github.io/cookiecutter-data-science/)
- [data science life cycle - Bing images](https://www.bing.com/images/search?q=data+science+life+cycle&form=HDRSC4&first=1)
- [(7) The Best Way to Organize Your Data Science Projects - YouTube](https://www.youtube.com/watch?v=MaIfDPuSlw8&t=443s)
## TODO
Since the purpose of this project is to automate as much as possible there will always be extra steps that could be save, here I leave a few that would be useful for me:
- [ ] Default `README.md` structure (title, overview, used tech, etc.)
- [ ] Automatically create the projects **venv**
- [ ] Config file manipulation (creation, load, . . .) should all be integrated on its own class to increase sustainability

