from setuptools import setup, find_packages

setup(
    # Application name:
    name="flask-docker",
    # Version number:
    version="1.0.0",
    # Application author details:
    author="Enrique Garcia",
    author_email="nitos_san@hotmail.com",
    # Packages
    packages=find_packages(),
    # Include additional files into the package
    include_package_data=True,
    # Details
    url="https://github.com/enriquedevs/flask-docker",
    description="Flask API with PostgreSQL and Docker",
)
