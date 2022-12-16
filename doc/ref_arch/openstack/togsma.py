# pylint: disable=missing-module-docstring,missing-class-docstring

import os
import shutil
import sys

from pybtex.database import parse_file
from sphinx.ext import intersphinx


class MockConfig:
    # pylint: disable=too-few-public-methods
    intersphinx_timeout: int = None
    tls_verify = False
    user_agent = None


class MockApp:
    # pylint: disable=too-few-public-methods,no-self-use
    # pylint: disable=missing-function-docstring
    srcdir = ''
    config = MockConfig()

    def warn(self, msg: str) -> None:
        print(msg, file=sys.stderr)


HEADER_REFERENCES = """References
----------

.. list-table:: References
   :widths: auto

   * - Ref
     - Doc Number
     - Title
"""

HEADER_BIBLIOGRAPHY = """Bibliography
------------

.. list-table:: Bibliography
   :widths: auto

   * - Ref
     - Document Title
     - Source
"""

invdata = intersphinx.fetch_inventory(MockApp(), '', "build/objects.inv")
bib_data = parse_file('refs.bib')

shutil.rmtree('gsma', ignore_errors=True)
os.mkdir('gsma')
shutil.copytree('figures', 'gsma/figures')
shutil.copy('conf.py', 'gsma/conf.py')
shutil.copy('refs.bib', 'gsma/refs.bib')

with open("gsma/references.rst", "w", encoding='utf-8') as references, open(
        "gsma/bibliography.rst", "w", encoding='utf-8') as bibliography:
    references.write(HEADER_REFERENCES)
    bibliography.write(HEADER_BIBLIOGRAPHY)
    i = 1

    for key in bib_data.entries:
        if 'howpublished' in bib_data.entries[key].fields:
            references.write(f"   * - [{i}]\n")
            references.write(
                f"     - {bib_data.entries[key].fields['howpublished']}\n")
            references.write(
                f"     - {bib_data.entries[key].fields['title']}\n")
        else:
            bibliography.write(f"   * - [{i}]\n")
            bibliography.write(
                f"     - {bib_data.entries[key].fields['title']}\n")
            bibliography.write(
                f"     - {bib_data.entries[key].fields['url']}\n")
        i = i + 1

filenames = ['chapters/chapter01.rst',
             'gsma/references.rst', 'gsma/bibliography.rst',
             'chapters/chapter02.rst', 'chapters/chapter03.rst',
             'chapters/chapter04.rst', 'chapters/chapter05.rst',
             'chapters/chapter06.rst', 'chapters/chapter07.rst',
             'chapters/chapter08.rst', 'chapters/chapter09.rst']

with open('gsma/index.rst', 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        with open(fname, encoding='utf-8') as infile:
            for line in infile:
                if (".. bibliography::" not in line.strip("\n") and
                        ":cited:" not in line.strip("\n")):
                    outfile.write(line)
            outfile.write('\n')

with open('gsma/index.rst', 'r', encoding='utf-8') as infile:
    filedata = infile.read()
    i = 1
    for key in bib_data.entries:
        if 'howpublished' in bib_data.entries[key].fields:
            filedata = filedata.replace(
                f":cite:p:`{bib_data.entries[key].key}`",
                f"`[{i}] <#references>`_")
        else:
            filedata = filedata.replace(
                f":cite:p:`{bib_data.entries[key].key}`",
                f"`[{i}] <{bib_data.entries[key].fields['url']}>`__")
        i = i + 1

    for key in sorted(invdata or {}):
        if 'std:label' in key:
            for entry, einfo in sorted(invdata[key].items()):
                if "chapters/" in entry:
                    filedata = filedata.replace(
                        f":ref:`{entry}`",
                        f"`{einfo[3]}`_")

    filedata = filedata.replace("../figures", "figures")

with open('gsma/index.rst', 'w', encoding='utf-8') as outfile:
    outfile.write(filedata)

os.remove("gsma/references.rst")
os.remove("gsma/bibliography.rst")
