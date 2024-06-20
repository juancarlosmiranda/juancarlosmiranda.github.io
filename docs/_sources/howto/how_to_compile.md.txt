# How To Compile this Site

This document contains instructions about how to build templates using [Sphinx](https://www.sphinx-doc.org). It is like my mental notes.

Tutorials:
* [Sphinx Tutorial: Build your first project](https://www.sphinx-doc.org/en/master/tutorial/index.html).
* [Creating your own documentation site with Sphinx and Slate](https://medium.com/@christianhettlage/creating-your-own-documentation-site-with-sphinx-6687391a5c92). A well explained tutorial on how to set up Sphinx for the first time. 
* [Sphinx Themes Sample](https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/). This site provides information about Sphinx Themes options.
* [Using Sphinx with Markdown instead of reST](https://stackoverflow.com/questions/2471804/using-sphinx-with-markdown-instead-of-rest). StackOverflow site with informations regarding to Sphinx.
* [Getting started with Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html).

Examples and configurations:
* [Sphinx Themes - Alabaster Sample](https://sphinx-themes.org/sample-sites/default-alabaster/). A good sample to start with.
* [Create great product documentation with Sphinx and Markdown](https://medium.com/@vvvlad42/create-great-documentation-with-sphinx-and-markdown-175c4017ae5a). Examples with configurations.
* [captum](https://github.com/pytorch/captum/) It is a good examples, this site generates documentation using Sphinx.

## Installing in Linux (TODO)
```
python3 -m venv ./juancarlosmiranda.github.io_venv
source ./juancarlosmiranda.github.io_venv/bin/activate
pip install --upgrade pip
```

Update environment requirements.
```
pip install sphinx sphinx-autobuild
pip install sphinx_rtd_theme
pip install myst-parser
```

Set the following in your existing Sphinx documentation’s ```conf.py``` file:
```
html_theme = 'sphinx_rtd_theme'
```

Generate the structure of the site.
```
sphinx-quickstart
sphinx-build -b html source/ docs/
make html
```

# Content management
Modify the files you want in ```./source/``` folder.

Compile the source code into HTML by applying the following:
```
sphinx-build -b html source/ docs/
make html
```
