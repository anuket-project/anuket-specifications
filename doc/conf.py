master_doc = 'index'
project = "Anuket Specifications"
html_title = "Anuket Specifications"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel'
             ]

exclude_patterns = [
    '**/.tox',
    'ref_arch',
    'ref_cert',
    'ref_impl',
    'ref_model',
    'tech',
    'gov/README.rst'
]
linkcheck_ignore = [
    'https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4',
    'https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf'
]
intersphinx_mapping = {
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/latest/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/latest/', None),
    'ref_impl_cntt-ri': ('https://cntt.readthedocs.io/projects/ri1/en/latest/', None),
    'ref_impl_cntt-ri2': ('https://cntt.readthedocs.io/projects/ri2/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4

numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

html_theme = "alabaster"
#html_sidebars = {
#    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
#}

html_static_path = ['_static']
templates_path = ['_templates']
#html_css_files = [
#    'css/custom.css',
#]
html_show_sourcelink = False
hto_name = 'Anuket Specifications'
hto_anchor_color = '16326c'
hto_font_family = '"Roboto", "Helvetica Neue", Helvetica, Arial, sans-serif'
html_theme_options = {
    # As defined in https://alabaster.readthedocs.io/en/latest/customization.html#theme-options
    'description': '',
    'fixed_sidebar': 'true',
    'logo': 'anuket-logo.png',
    'logo_name': '',
    'github_button': 'true',
    'github_repo': 'https://github.com/cntt-n/cntt',
    'github_user': '',
    'show_powered_by': 'true',
    'anchor': hto_anchor_color, 
    'anchor_hover_fg': hto_anchor_color,
    'anchor_hover_bg': 'a58345',
    'caption_font_family': hto_font_family,
    'font_family': hto_font_family,
    'logo_text_align': 'center',

}

# Inverse png
#html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'
