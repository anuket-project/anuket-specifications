project = 'Anuket Reference Architecture for OpenStack based cloud infrastructure (RA1)'
copyright = '2022, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
exclude_patterns = [
    '.tox',
    'README.rst',
    'gsma/index.rst'
]
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex'
]
html_theme = "piccolo_theme"
linkcheck_ignore = [
    "https://www.cisecurity.org/cis-benchmarks/",
    "https://www.iso.org/obp/ui/",
    'http://127.0.0.1',
    'https://www.sdxcentral.com',
    'https://ntia.gov'
]
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4

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


numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
latex_theme = 'howto'
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
