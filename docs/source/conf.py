import os
import sys

import alabaster
import hdfscm

# Project settings
project = 'hdfscm'
copyright = '2019, Jim Crist'
author = 'Jim Crist'
release = version = hdfscm.__version__

source_suffix = '.rst'
master_doc = 'index'
language = None
pygments_style = 'sphinx'
exclude_patterns = []

# Sphinx Extensions
docs = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(docs, 'sphinxext'))
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.extlinks',
              'sphinx.ext.napoleon',
              'autodoc_traitlets']

numpydoc_show_class_members = False

extlinks = {
    'issue': ('https://github.com/jcrist/hdfscm/issues/%s', 'Issue #'),
    'pr': ('https://github.com/jcrist/hdfscm/pull/%s', 'PR #')
}

# Sphinx Theme
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
templates_path = ['_templates']
html_static_path = ['_static']
html_theme_options = {
    'description': 'A Jupyter ContentsManager for storing content on HDFS',
    'github_button': True,
    'github_count': False,
    'github_user': 'jcrist',
    'github_repo': 'hdfscm',
    'travis_button': True,
    'show_powered_by': False,
    'page_width': '960px',
    'sidebar_width': '250px',
    'code_font_size': '0.8em'
}
html_sidebars = {
    '**': ['about.html',
           'navigation.html',
           'help.html',
           'searchbox.html']
}
