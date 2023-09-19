# Automatic Project Structure Generator

## Project Overview
Every coding project has unique goals, different requirements and specific features that are not shared across field-related projects. However, if I have learned anything about computer science is that organization and structure consistency is key to success, that is why this repo is focused on developing an automatic initial workplace so that the structure and initial steps of every project remain consistent. Due to my specialization, there are two main branches of projects that I work on in a day to day fashion: **APPs**, **API**, . . .; or, what I call, **AP** projects and **Data Science** (DS) projects.
## Shared Items
Despite the differences between projects there are always some commonalities.
- `.gitignore`: Avoid pushing files like `.ipynb_checkpoints/`, `.obsidian`, etc.
- `./images/`: Images used on the readmes.
- `./test/`: Include API, APP, models, . . . tests.
- `config.json`: 
## AP Projects
AP projects consist on the `main.py` file located in the project folder and surrounded by packages that feed `main.py` the necessary tools to work properly. Every package has associated both `constants.py` and `utils.py` files which I find necessary to provide support to `package.py`, and, of course a `README.md` that further explains the package functionality.
### Example Structure
```bash
├── AP Project
│   ├── .gitignore  
│   ├── images/
│   ├── test/ 
│   ├── Package Name
│   │   ├── __init.py__
│   │   ├── constants.py
│   │   ├── utils.py
│   │   ├── package_name.py
│   │   └── README.md
│   ├── main.py
│   └── README.md
└── 
```

## DS Projects
TODO
- [Home - Cookiecutter Data Science (drivendata.github.io)](http://drivendata.github.io/cookiecutter-data-science/)
- [data science life cycle - Bing images](https://www.bing.com/images/search?q=data+science+life+cycle&form=HDRSC4&first=1)
- [(7) The Best Way to Organize Your Data Science Projects - YouTube](https://www.youtube.com/watch?v=MaIfDPuSlw8&t=443s)
## TODO
Since the purpose of this project is to automate as much as possible there will always be extra steps that could be save, here I leave a few that would be useful for me:
- [ ] Default `README.md` structure (title, overview, used tech, etc.)
- [ ] Automatically create the projects **venv**.

