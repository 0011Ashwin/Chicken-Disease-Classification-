# importing libraries
import os
from pathlib import Path
import logging

# logging configuration, info -> date -> timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

# list of files to be created for project 
list_of_files = [
    ".github/workflows/.gitkeep", # Placeholder file to keep the directory structure in Git
    f"src/{project_name}/__init__.py", # Init file for the main project module
    f"src/{project_name}/components/__init__.py", # Init file for the components submodule
    f"src/{project_name}/utils/__init__.py", # Init file for the untils submodule
    f"src/{project_name}/config/__init__.py", # Init file for the config submodule
    f"src/{project_name}/config/configuration.py", # Configuration file fir the project 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")