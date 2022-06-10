project = 'Anuket Kubernetes based Reference Architecture (RA2)'
copyright = '2022, Anuket'
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
    "https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md",
    "https://github.com/opencontainers/runtime-spec/blob/master/config.md",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en",
    "https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en"
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_impl2': ('https://cntt.readthedocs.io/projects/ri2/en/latest/', None),
    'ref_arch1': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
