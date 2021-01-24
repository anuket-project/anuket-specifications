# © 2020 Nokia
#
# Licensed under the Apache License 2.0
#
# SPDX-License-Identifier: Apache-2.0

###
# A sphinx extension to support the relative linking of html files.
# Inspired by and partly copyed from 
# https://github.com/firegurafiku/sphinxcontrib-divparams/
###

#from docutils import nodes
#from docutils.parsers.rst import Directive
#from sphinx.locale import _
#from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging
from sphinx.environment import NoUri

import bs4
import shutil
import os
import re

logger = logging.getLogger(__name__)


def transform_html(soup):
    links = soup.find_all("a")
    for link in links:
        #logger.info("l: " + str(link))
        if link.has_attr("href"):
            logger.debug("l: " + str(link['href']))
            if "://" not in link['href']:
                res = re.search("(\.md\#|\.md$)", link['href'])
                if res:
                    corect_link = link['href'].replace(".md", ".html")
                    logger.debug("  c: correct link is " + corect_link)
                    link['href'] = corect_link
                else: 
                    logger.debug("  c: no match of .md")
            else: 
                logger.debug("  c: this is an absolulte link")
        
        logger.debug("l: done")

def relative_link_corrector(app, exception):
    logger.info("relative-link-corrector is correcting relative links")

    # Don't risk doing anything if Sphinx failed in building HTML.
    if exception is not None:
        return

    # Find all files eligible for DOM transform.
    # See also: http://stackoverflow.com/a/33640970/1447225
    target_files = []
    for doc in app.env.found_docs:
        target_filename = "#"
        try:
            target_filename = app.builder.get_target_uri(doc)
        except NoUri:
            continue
        if '#' in target_filename:
            logger.info("Skipping")
            continue

#        logger.info("tfn1: " + target_filename)
        target_filename = os.path.join(app.outdir, target_filename)
#        logger.info("tfn2: " + target_filename)
        target_filename = os.path.abspath(target_filename)
#        logger.info("tfn3: " + target_filename)
        target_files.append(target_filename)

    for fn in target_files:
        try:
            with open(fn, mode="rb") as f:
                soup = bs4.BeautifulSoup(f.read(), "html.parser")

            transform_html(soup)
            html = soup.prettify(encoding=app.config.html_output_encoding)

            with open(fn, mode='wb') as f:
                f.write(html)

        except Exception as exc:
            app.warning("Exception raised during HTML tweaking: " + str(exc))

def setup(app):
    app.connect('build-finished', relative_link_corrector)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }