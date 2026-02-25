from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Ecommerce Product Recommender",
    version="0.1",
    author="Dilip Rathod",
    packages=find_packages(),
    install_requires = requirements,
)