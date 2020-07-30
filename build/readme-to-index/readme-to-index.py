# © 2020 Nokia
#
# Licensed under the Apache License 2.0
#
# SPDX-License-Identifier: Apache-2.0

###
# A sphinx extension to copy generated README.html files to index.html.
###

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

import shutil
import os
logger = logging.getLogger(__name__)


def readme_to_index(app, exception):
    logger.info("readme_to_index target directory is " + app.outdir)
    for dirpath, dirnames, filenames in os.walk(app.outdir):
        for name in filenames:
            if name == "README.html":
                logger.info(" -" + os.path.join(dirpath, name))
                target = dirpath + "/index.html"
                source = dirpath + "/README.html"
                if not os.path.isfile(target):
                    logger.info("Copying " + source + " to " + target)
                    shutil.copy(source, target, follow_symlinks=True)
                else:
                    logger.info("  -" + target + " already exist. NOT writing it over.")


def setup(app):

    app.connect('build-finished', readme_to_index)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }