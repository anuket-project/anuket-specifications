project = 'Anuket Reference Architecture for OpenStack based cloud infrastructure (RA1)'
copyright = '2021, Anuket'
author = 'Anuket'
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
linkcheck_ignore = [
    "https://www.cisecurity.org/cis-benchmarks/",
    "https://www.iso.org/obp/ui/",
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
latex_theme = 'howto'
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
