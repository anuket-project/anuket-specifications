import os
import sys
import sphinx_rtd_theme

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'CNTT-CNTT'

sys.path.append(os.path.abspath("../build/direct-copy"))
sys.path.append(os.path.abspath("../build/readme-to-index"))
sys.path.append(os.path.abspath("../build/relative-link-corrector"))

extensions = ['direct-copy', 
              'readme-to-index', 
              'relative-link-corrector',
              'sphinx_markdown_tables', 
              'sphinx_rtd_theme']

direct_copy_directories = ['/gov/figures', 
                           '/ref_model/figures', 
                           '/ref_arch/figures', 
                           '/ref_arch/kubernetes/figures', 
                           '/ref_arch/openstack/figures', 
                           '/ref_cert/RC1/figures', 
                           '/ref_cert/RC2/figures', 
                           '/ref_impl/cntt-ri/figures', 
                           '/ref_impl/cntt-ri2/figures',
                           '/ven_impl/figures', 
                           '/common/figures'] 

html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]