project = 'Anuket OpenStack based Reference Architecture'
copyright = '2021, Anuket'
author = 'Anuket'
exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]
html_theme = "sphinx_material"
linkcheck_ignore = [
    "https://www.cisecurity.org/cis-benchmarks/",
    "https://www.iso.org/obp/ui/",
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
latex_theme = 'howto'
