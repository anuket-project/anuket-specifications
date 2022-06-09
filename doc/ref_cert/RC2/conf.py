project = 'Anuket Reference Conformance for Kubernetes (RC2)'
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
    'http://127.0.0.1'
]
intersphinx_mapping = {
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/stable-moselle/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
latex_theme = 'howto'
