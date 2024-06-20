project = 'Juan Carlos blog\'s'
copyright = '2022, Juan Carlos Miranda'
author = u'Juan Carlos Miranda'
version = u'0.1'
release = u'0.1'


extensions = [
    'sphinx.ext.mathjax',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
#html_theme = 'press'
html_static_path = ['_static']
#html_static_path = ['_codes']


#from recommonmark.parser import CommonMarkParser
#source_parsers = {
#    '.md': CommonMarkParser
#}

# source_suffix = ['.rst', '.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
