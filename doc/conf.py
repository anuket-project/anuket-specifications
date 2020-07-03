import os
import sys

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'CNTT-CNTT'

sys.path.append(os.path.abspath("../direct-copy"))
sys.path.append(os.path.abspath("../readme-to-index"))
sys.path.append(os.path.abspath("../relative-link-corrector"))

extensions = ['direct-copy', 
              'readme-to-index', 
              'relative-link-corrector',
              'sphinx_markdown_tables']

direct_copy_directories = ['/gov/figures', 
                           '/ref_model/figures', 
                           '/ref_arch/figures', 
                           '/ref_arch/kubernetes/figures', 
                           '/ref_arch/openstack/figures', 
                           '/ref_cert/lfn/figures', 
                           '/ref_cert/RC2/figures', 
                           '/ref_impl/cntt-ri/figures', 
                           '/ref_impl/cntt-ri2/figures',
                           '/tech/figures', 
                           '/ven_impl/figures'] 
