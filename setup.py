from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME= "Dog_and_Cat_Classifier"
Author_User_Name = "Sijibomiaol"
SRC_REPO = "Dog_and_Cat_Classifier"
Author_Email= "aderinlewomoses@gmail.com"

setup(

    name= SRC_REPO, 
    version= __version__,
    author= Author_User_Name,
    author_email=Author_Email,
    description= "A small python package for CNN app",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{Author_User_Name}/{REPO_NAME}"},
    package_dir= {"": "src"},
    packages= find_packages(where="src")
    
)
    