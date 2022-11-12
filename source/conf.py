project = 'Notes and Recipes in Computer Science'
copyright = '2022, Juan Carlos Miranda'
author = u'Juan Carlos Miranda'
version = u'0.1'
release = u'0.1'


extensions = [
    'sphinx.ext.mathjax'
]

templates_path = ['_templates']
exclude_patterns = []


#html_theme = 'alabaster'
html_theme = 'press'

html_static_path = ['_static']

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser
}

source_suffix = ['.rst', '.md']

