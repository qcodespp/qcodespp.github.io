import os

text1='# Configuration file for the Sphinx documentation builder.\n#\n# For the full list of built-in configuration values, see the documentation:\n# https://www.sphinx-doc.org/en/master/usage/configuration.html\n\n# -- Project information -----------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information\n\nproject = \'qcodes++\'\ncopyright = \'2025, qcodes++\'\nauthor = \'qcodes++\'\nrelease = \'0.1.11\'\nversion = \'0.1.11\'\n\nhtml_favicon = \'qcppfavicon.svg\'\n\n# -- General configuration ---------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration\n\nextensions = [\n    \'sphinx.ext.duration\',\n    \'sphinx.ext.doctest\',\n    \'sphinx.ext.autodoc\',\n    \'sphinx.ext.autosummary\',\n    \'autoapi.extension\',\n]\n\nautoapi_dirs=[\'C:/git/qcodespp/qcodespp\']\nautoapi_options=[ \'members\', \'undoc-members\',\'show-inheritance\', \'show-module-summary\', \'special-members\', \'imported-members\']\ntemplates_path = [\'_templates\']\nautoapi_keep_files = True\n\nexclude_patterns = [\'_build\', \'_templates\', "**.ipynb_checkpoints"]\n\n# -- Options for HTML output -------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output\n\nhtml_theme = \'sphinx_rtd_theme\'\n#html_static_path = [\'_static\']\n'

text2='# Configuration file for the Sphinx documentation builder.\n#\n# For the full list of built-in configuration values, see the documentation:\n# https://www.sphinx-doc.org/en/master/usage/configuration.html\n\n# -- Project information -----------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information\n\nproject = \'qcodes++\'\ncopyright = \'2025, qcodes++\'\nauthor = \'qcodes++\'\nrelease = \'0.1.11\'\nversion = \'0.1.11\'\n\nhtml_favicon = \'qcppfavicon.svg\'\n\n# -- General configuration ---------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration\n\nextensions = [\n    \'sphinx.ext.duration\',\n    \'sphinx.ext.doctest\',\n    \'sphinx.ext.autodoc\',\n    \'sphinx.ext.autosummary\']\n\nexclude_patterns = [\'_build\', \'_templates\', "**.ipynb_checkpoints"]\n\n# -- Options for HTML output -------------------------------------------------\n# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output\n\nhtml_theme = \'sphinx_rtd_theme\'\n#html_static_path = [\'_static\']\n'

conf_path ='C:/git/qcodespp.github.io/docs/source/conf.py'

with open(conf_path, 'r', encoding='utf-8') as f:
    current = f.read()

if current == text1:
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(text2)
    print('conf.py updated to exclude autoapi')
elif current == text2:
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(text1)
    print('conf.py updated to include autoapi')