# why setup.py
# we make setup.py bcoz we want to make our src folder as local package
# jha bhi __init__.py file hogi wha  yeuse local packag m ban dega 
with open("README.md", 'r',encoding='utf-8') as f:
    long_description=f.read()

__version__= "0.0.0"

REPO_NAME='chest-cancer-classification-using-DVC-and-MLFlow'
AUTHOR_USER_NAME='sagar-76'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL= 'sagarbhagwani76@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for cnn app',
    Long_description=long_description,
    Long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)