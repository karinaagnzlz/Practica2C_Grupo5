#!/usr/bin/python

from setuptools import setup
from setuptools import find_packages


def get_version():
    with open("Practica2C_Grupo5/__init__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


def get_requires():
    requirements_list = []
    with open("requirements.txt") as f:
        for line in f:
            requirements_list.append(line)
    return requirements_list


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="Practica2C_Grupo5",
    version=get_version(),
    description="Practica2C_Grupo5",
    long_description=readme,
    author="Rómulo Rodríguez",
    packages=find_packages(),
    install_requires=get_requires(),
    include_package_data=True,
)