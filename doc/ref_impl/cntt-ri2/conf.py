import sphinx_material

project = 'Anuket Reference Implementation based on RA2 specifications (RI2)'
html_title = "Anuket Reference Implementation based on RA2 specifications (RI2)"
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
linkcheck_ignore = [
    'http://127.0.0.1'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/stable-nile/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/stable-nile/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/stable-nile/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/stable-nile/', None),
    'ref_impl_cntt-ri': ('https://cntt.readthedocs.io/projects/ri1/en/stable-nile/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
