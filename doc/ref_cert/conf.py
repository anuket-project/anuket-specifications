project = 'Anuket Reference Conformance'
copyright = '2021, Anuket'
author = 'Anuket'
exclude_patterns = [
    '.tox',
    'build',
    'RC2',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]
html_theme = "piccolo_theme"
linkcheck_ignore = [
    'http://127.0.0.1',
    'https://www.sdxcentral.com'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
