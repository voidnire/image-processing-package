from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    page_description = f.read()


with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines() 

setup(
    name="package_name",
    version="0.0.1",
    author="erin_dante",
    author_email="erin@email.com",
    description="Short description",
    long_description=page_description,
    url="githubrepo",
    packages=find_packages(),
    install_requires=requirements.txt,
    python_requires='>=3.8',
)


# pip install --upgrade pip
# pip install --user twine
# pip install --user setuptools


# python setup.py sdist bdist_wheel
# twine upload --repository pypi dist/*

# PUBLICAÇAO:
# https://pypi.org/manage/projects/image-processing-package/releases/