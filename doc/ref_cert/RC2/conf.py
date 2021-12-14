project = 'Anuket Reference Conformance for Kubernetes (RC2)'
copyright = '2021, Anuket'
author = 'Anuket'
exclude_patterns = [
    '.tox'
]
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx'
]
html_theme = "sphinx_rtd_theme"
linkcheck_ignore = [
    'http://127.0.0.1'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}
