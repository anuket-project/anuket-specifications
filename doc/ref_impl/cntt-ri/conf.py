project = 'Anuket Reference Implementation based on RA1 specifications (RI1)'
html_title = "Anuket Reference Implementation based on RA1 specifications (RI1)"
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
    'https://trex-tgn.cisco.com',
# The following items are added due to the flackyness of the OPNFV build servers
# they can be removed as soon as the build server issues are fixed.
# Related issue: https://jira.linuxfoundation.org/plugins/servlet/desk/portal/2/IT-25549
    'https://build.opnfv.org/ci/view/cntt/',
    'http://artifacts.opnfv.org/',
    'https://build.opnfv.org/', 
    'https://wiki.lfnetworking.org/'

]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
