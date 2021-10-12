#!/bin/python3

import logging
import argparse
import glob
import os
import re

def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    idText = "A script to run before doing the conversion from md to rst."
    logger.info(idText)
    parser = argparse.ArgumentParser(description=idText)
    parser.add_argument('directory', default="",
                        help='The directory where all the .md files should be processed.')
    parser.add_argument('--debug', action="store_true",
                        help='Print debug logs.')

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging is ON")
    fileList = glob.glob(args.directory + '*.md')
    for filename in fileList:
        logger.info("Filename is " + filename)
        if re.match(".*-mod.md", filename):
            logger.debug("Mod file found, deleting it.")
            os.remove(filename)
            continue
        filenameNew = filename.replace(".md", "-mod.md")
        logger.debug("Modified filename is " + filenameNew)
        if os.path.exists(filenameNew):
            logger.debug("Removing " + filenameNew)
            os.remove(filenameNew)
        fIn = open(filename, 'r')
        fOut = open(filenameNew, 'w')
        lineNumber = 0
        state = {}
        for line in fIn:
            #logger.debug("Line is " + line)
            lineNumber = lineNumber + 1
            state["line"] = line
            if re.match("## Table of Contents", line):
                #logger.info(" " + str(lineNumber) + " ToC found")
                state["in-toc"] = True
                continue

            if ("in-toc" in state) and state["in-toc"]:
                #logger.debug(" " + str(lineNumber) + " state in-toc")
                if re.match('^\s+$', line):
                    if ("content-after-toc" in state) and state["content-after-toc"]:
                        # In some cases thre is an empty line just after the ToC header, so
                        # we expect to have some content before the new line what indicates the 
                        # end of ToC
                        del state["in-toc"]
                else:
                    state["content-after-toc"] = True
                    continue
            logger.debug("Out line is " + state["line"])
            print(state["line"], file = fOut, end = "")
        
        fIn.close()
        fOut.close()

if __name__ == "__main__":
    main()
