# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'qcodes++'
copyright = '2025, qcodes++'
author = 'qcodes++'
release = '0.1.0'
version = '0.1.0'

html_favicon = 'qcppfavicon.svg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary']
#     'autoapi.extension',
# ]

# autoapi_dirs=['C:/git/qcodespp/qcodespp']
# autoapi_options=[ 'members', 'undoc-members','show-inheritance', 'show-module-summary', 'special-members', 'imported-members']
# templates_path = ['_templates']
# autoapi_keep_files = True

exclude_patterns = ['_build', '_templates', "**.ipynb_checkpoints"]
autosummary_generate = False
# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
#     'show-inheritance': True,
#     'show-module-summary': True,
#     'special-members': '__init__'
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
