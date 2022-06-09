import sphinx_material

master_doc = 'index'
project = "Anuket Specifications"
html_title = "Anuket Specifications"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'

extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel'
             ]
html_theme = "sphinx_material"
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()

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
    'ref_arch',
    'ref_cert',
    'ref_impl',
    'ref_model',
    'tech'
]

linkcheck_ignore = [
    'https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4',
    'https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf'
]


intersphinx_mapping = {
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/stable-moselle/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/stable-moselle/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/stable-moselle/', None),
    'ref_cert_RC1': ('https://cntt.readthedocs.io/projects/rc1/en/stable-moselle/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/stable-moselle/', None),
    'ref_impl_cntt-ri': ('https://cntt.readthedocs.io/projects/ri1/en/stable-moselle/', None),
    'ref_impl_cntt-ri2': ('https://cntt.readthedocs.io/projects/ri2/en/stable-moselle/', None)
}

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
