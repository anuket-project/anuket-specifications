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

extensions = ['direct-copy', 
              'readme-to-index']

direct_copy_directories = ['/gov/figures', 
                           '/ref_model/figures']
