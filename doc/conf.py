master_doc = 'index'
project = "Anuket Specifications"
html_title = "Anuket Specifications"
copyright = '2023, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel',
              'sphinxcontrib.bibtex'
             ]

exclude_patterns = [
    '**/.tox',
    '**/README.rst'
]
linkcheck_ignore = [
    'https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4',
    'https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf',
    'https://ntia.gov',
    'https://www.ngmn.org/wp-content/uploads/Publications/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf',
    'https://wiki.lfnetworking.org/'
]

# temporarly I just add all intersphinx mappings needed. later these should be replaced with a single intersphinx to the
# whole document itself.
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/latest/', None),
    'ref_impl_cntt-ri': ('https://cntt.readthedocs.io/projects/ri1/en/latest/', None),
    'ref_impl_cntt-ri2': ('https://cntt.readthedocs.io/projects/ri2/en/latest/', None)

}


autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4

bibtex_bibfiles = [
    'ref_model/refs.bib',
    'ref_arch/openstack/refs.bib', 
    'ref_arch/kubernetes/refs.bib'
    ]
bibtex_default_style = 'unsrt'

numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

html_theme = "piccolo_theme"

html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = [
    'custom.css',
]

html_show_sourcelink = False
html_theme_options = {
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Inverse png
html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'
