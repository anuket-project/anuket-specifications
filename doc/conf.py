import os
import sys
import sphinx_material

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

templates_path = ['_templates']

master_doc = 'index'
project = "Anuket Specifications"
html_title = "Anuket Specifications"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'

extensions = ['sphinxcontrib.readme-to-index', 
              'sphinxcontrib.relative-link-corrector',
              'sphinxcontrib.direct-copy',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel',
              'sphinx_markdown_tables',
              'sphinx_material'
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

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    'repo_name': 'Material for Sphinx',
    'nav_title': 'Anuket Specifications',
     # Set the color and the accent color
    'color_primary': 'white',
    'color_accent': 'teal',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
    'nav_links': [
        {
            'href': 'https://docs.opnfv.org/',
            'internal': False,
            'title': 'Anuket Project Documentation'
        }
    ]
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
autosectionlabel_maxdepth = 4
