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

extensions = ['sphinxcontrib.readme-to-index', 
              'sphinxcontrib.relative-link-corrector',
              'sphinxcontrib.direct-copy',
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
