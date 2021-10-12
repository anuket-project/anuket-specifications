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

    for filename in glob.glob(args.directory + '*.md'):
        logger.info("Filename is " + filename)
        filenameNew = filename.replace(".md", "-mod.md")
        logger.debug("Modified filename is " + filenameNew)
        if os.path.isfile(filenameNew):
            logger.debug("Removing " + filenameNew)
            os.remove(filenameNew)
        fIn = open(filename, 'r')
        fOut = open(filenameNew, 'w')
        lineNumber = 0
        for line in fIn:
            #logger.debug("Line is " + line)
            if re.match("Table of Contents", line):
                logger.info(" " + lineNumber + "ToC found")
                newLine = ""

            else:
                newLine = line

            lineNumber = lineNumber + 1
            print(newLine, file = fOut)
        
        fIn.close()
        fOut.close()

if __name__ == "__main__":
    main()
