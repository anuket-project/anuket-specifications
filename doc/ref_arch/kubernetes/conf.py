project = 'Anuket Reference Architecture for Kubernetes based cloud infrastructure (RA2)'
copyright = '2023, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex'
]

html_theme = "piccolo_theme"

linkcheck_ignore = [
    "https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md",
    "https://github.com/opencontainers/runtime-spec/blob/master/config.md",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en",
    "https://ntia.gov/page/software-bill-materials"
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_impl2': ('https://cntt.readthedocs.io/projects/ri2/en/latest/', None),
    'ref_arch1': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

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

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'