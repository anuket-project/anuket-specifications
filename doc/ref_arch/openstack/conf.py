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
    'https://ntia.gov',
# The following items are added due to the flackyness of the OPNFV build servers
# they can be removed as soon as the build server issues are fixed.
# Related issue: https://jira.linuxfoundation.org/plugins/servlet/desk/portal/2/IT-25549
    'https://build.opnfv.org/',
    'https://docs.opnfv.org/en/stable-hunter/_images/OPNFV_testing_working_group.png',
    'http://artifacts.opnfv.org/',
    'https://build.opnfv.org/ci/job/functest-wallaby-zip/4/console'
###
]
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
latex_theme = 'howto'
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
