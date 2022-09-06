project = 'Anuket Reference Implementation for Kubernetes'
html_title = "Anuket Reference Implementation for Kubernetes"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]
linkcheck_ignore = [
    'http://127.0.0.1',
    'https://trex-tgn.cisco.com'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/stable-moselle/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/stable-moselle/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/stable-moselle/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
