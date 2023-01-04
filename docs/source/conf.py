# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
sys.path.insert(0, os.path.abspath('../..'))



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'degrotesque'
copyright = '2023, Daniel Krajzewicz'
author = 'Daniel Krajzewicz'
release = '2.0'
version = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
# make same navigation on all pages ("global")
# https://stackoverflow.com/questions/18969093/how-to-include-the-toctree-in-the-sidebar-of-each-page
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

autosummary_imported_members = True
autosummary_generate = True



templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output

html_theme = 'alabaster'
html_static_path = ['_static']


# -- Options for EPUB output
epub_show_urls = 'footnote'

