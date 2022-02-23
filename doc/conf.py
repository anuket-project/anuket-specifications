import os
import sys
#import sphinx_rtd_theme
import sphinx_bootstrap_theme

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

templates_path = ['_templates']

master_doc = 'index'
project = ''
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'

extensions = ['sphinxcontrib.readme-to-index', 
              'sphinxcontrib.relative-link-corrector',
              'sphinxcontrib.direct-copy',
              'sphinx_markdown_tables', 
              'sphinx_rtd_theme',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel'
             ]

direct_copy_directories = ['/gov/figures', 
                           '/ref_model/figures', 
                           '/ref_arch/figures', 
                           '/ref_arch/kubernetes/figures', 
                           '/ref_arch/openstack/figures', 
                           '/ref_cert/RC1/figures', 
                           '/ref_cert/RC2/figures', 
                           '/ref_impl/cntt-ri/figures', 
                           '/ref_impl/cntt-ri2/figures',
                           '/ven_impl/figures', 
                           '/common/figures'] 

html_theme = "bootstrap"
#html_theme = "sphinx_rtd_theme"

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_sidebars = {'**': ['my_custom_sidebar.html', 'relations.html'],}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    'bootswatch_theme': "journal",
    'navbar_sidebarrel': False,
}

html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'

exclude_patterns = [
    '**/.tox',
]

intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3