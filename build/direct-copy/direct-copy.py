# © 2020 Nokia
#
# Licensed under the Apache License 2.0
#
# SPDX-License-Identifier: Apache-2.0

####
# A sphinx extension to copy files directly from the source directory to the target
# directory. 
# Usage: 
#  1) Enable `direct-copy` extension in your conf.py
#  2) Add a list of directories to be copyed in the `direct_copy_directories` parameter.
####

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

import shutil

logger = logging.getLogger(__name__)

def direct_copy(app, exception):
    logger.info("direct_copy source directory is " + app.srcdir + ", target directory is " + app.outdir)
    for dir in app.config.direct_copy_directories:
        logger.info('Direct copying '+ dir)
        shutil.copytree(src=app.srcdir + dir, dst=app.outdir + dir, symlinks=True)

def setup(app):
    app.add_config_value('direct_copy_directories', False, 'html')

    app.connect('build-finished', direct_copy)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }