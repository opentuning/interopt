# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configuration file for the Sphinx documentation builder.
import os
import sys
from pathlib import Path

# Add the project root directory to the Python path so Sphinx can find the package
sys.path.insert(0, str(Path(__file__).parents[1].resolve()))

# Project information
project = 'InterOpt'
copyright = '2024, Jacob O. Torring'
author = 'Jacob O. Torring'
release = '0.3'

# Mock imports for packages that might not be available during doc building
autodoc_mock_imports = [
    'grpc',
    'numpy',
    'pandas',
    'catboost',
    'sklearn',
    'fastapi',
    'uvicorn',
    'requests',
    'pyperclip'
]

# Extension configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints'
]

# Napoleon settings for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# General settings
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
