project = 'Anuket Reference Model (RM)'
copyright = '2022, Anuket. Licensed under CC BY 4.0'
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
html_theme = "sphinx_material"
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}
linkcheck_ignore = [
    'https://www.iso.org',
    'https://www.etsi.org',
    'https://infocentre2.gsma.com',
    'https://nplang.org',
    'https://ntia.gov', 
    'https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf'
]
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
