# import os
# import pathlib
# from pathlib import Path
# import logging

# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name='cnnClassifer'
# # now we will gve list of files which we want to create

# list_of_files=[
#     ".github/workflows/.gitkeep",
#     #whenenver we do cicd deployment we need this github folder
#     # in this we will make main.yaml which wiill follow some commands
#     f"src/{project_name}/__init__.py",
#     # in src folder i make folder project name
#     # in project name i make constructor which will help
#     # me us create  in local package
#     f"src/{project_name}/components/__init__.py",
#     # will use for related model testing and all
#     f"src/{project_name}/utils/__init__.py",

#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/constants/__init__.py",
#     "config/config.yaml",
#     "dvc.yaml",
#     "params.yaml",
#     "requirements.txt",
#     "setup.py",
#     'research/trials.ipynb',
#     "template/index.html"
#     # index.html m code krenge for  streamlit app


# ]
# for filepath in list_of_files:
#     filepath=Path(filepath)
#     # this Path from path lib cn hanfdle all errors
#     # dosnt matter you are in lenux, mac, or Windows
#     filedir,filename=os.path.split(filepath)

#     if filedir !=None:
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f'Creating directory;{filedir} for the file: {filename}')
#         # this code will create the source folder

#     # lets create the files inside the source folder
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
#         with open(filepath, "w") as f:
#             pass
#             logging.info(f'Creating empty file: {filepath}')
#     else:
#         logging.info(f"{filename} is already exists")

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
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
