from setuptools import setup
from typing import List

PROJECT_NAME ="housing-prediction"
VERSION = "0.0.4"
AUTHOR = 'Vijit'
DESCRIPTION ="this is 1st ml project"
PACKAGES =["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME)as requirement_file:
        return requirement_file.readlines().remove("-e .")
setup(
    name = "housing-prediction",
    version=VERSION,
    author='Vijit',
    description=DESCRIPTION,
    packages= PACKAGES,
    install_requires = get_requirements_list()
)

