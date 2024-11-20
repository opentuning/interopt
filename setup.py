# setup.py
from setuptools import setup, find_packages

setup(
    name='interopt',
    version='0.2.0',
    author='Jacob Odgård Tørring',
    author_email='jacob.torring@ntnu.no',
    packages=find_packages(),
    license='LICENSE',
    description='An interoperability layer for black-box optimization',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    # Include requirements from requirements.txt
    install_requires=open('requirements.txt', encoding='utf-8').read().splitlines()
)
