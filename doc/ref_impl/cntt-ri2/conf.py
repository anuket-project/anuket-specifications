import sphinx_material

project = 'Anuket Reference Implementation for Kubernetes'
html_title = "Anuket Reference Implementation for Kubernetes"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'

exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx_material',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

html_theme = "sphinx_material"
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_static_path = ['../../_static']
html_logo = '../../_static/anuket-logo.png'
html_favicon = '../../_static/favicon.ico'
#html_css_files = [
#    'css/custom.css',
#]

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

linkcheck_ignore = [
        'http://127.0.0.1'
]

intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/latest/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/latest/', None),
    'ref_impl_cntt-ri': ('https://cntt.readthedocs.io/projects/ri1/en/latest/', None)
}

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
