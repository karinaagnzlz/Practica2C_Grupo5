#!/usr/bin/python

from setuptools import setup
from setuptools import find_packages


def get_version():
    with open("practica2c_grupo5_simple_ws/__init__.py") as f:
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
    name="practica2c_grupo5_simple_ws",
    version=get_version(),
    description="practica2c_grupo5_simple_ws",
    long_description=readme,
    author="Rómulo Rodríguez",
    packages=find_packages(),
    install_requires=get_requires(),
    include_package_data=True,
)
