#!/bin/python3
####
# Copyright 2021 Nokia
# Licensed under the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
####
# A script to mass modify Anuket specification md files before converting them to rst. 
# TODO:
#  - Remove `[<< Back](../)`-s 
#  - Doublechec which raw html-s can be removed of converted to markdown. 
#    In case of complete converision is not possible, like in case of images
#    with scaling. These should be handled in a post conversion script.  


import argparse
import glob
import logging
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
    filePattern = "{}/*.md".format(args.directory)
    logger.info("File pattern is {}".format(filePattern))
    fileList = glob.glob(filePattern)
    for filename in fileList:
        logger.info("Filename is {}".format(filename))
        if re.match(".*-mod.md", filename):
            logger.debug("Mod file found, deleting it.")
            os.remove(filename)
            continue
        filenameNew = filename.replace(".md", "-mod.md")
        logger.debug("Modified filename is {}".format(filenameNew))
        if os.path.exists(filenameNew):
            logger.debug("Removing {}".format(filenameNew))
            os.remove(filenameNew)
        fIn = open(filename, 'r')
        fOut = open(filenameNew, 'w')
        lineNumber = 0
        state = {}
        for line in fIn:
            #logger.debug("Line is {}".format(line))
            lineNumber = lineNumber + 1
            state["line"] = line
            if re.match("## Table of Contents", line):
                #logger.info(" {%d}: ToC found".format(lineNumber))
                state["in-toc"] = True
                continue

            if ("in-toc" in state) and state["in-toc"]:
                #logger.debug(" {%d} state in-toc".format(lineNumber))
                if re.match('^\s+$', line):
                    if ("content-after-toc" in state) and state["content-after-toc"]:
                        # In some cases thre is an empty line just after the ToC header, so
                        # we expect to have some content before the new line what indicates the 
                        # end of ToC
                        del state["in-toc"]
                else:
                    state["content-after-toc"] = True
                    continue
            # ## 7.2 Gap analysis
            elif (re.match("^#+\s+[0-9A-Z\.]+\s+", line)):
                #logger.debug("Header line: " + line)
                result = re.sub(r"(^#+\s+)([0-9A-Z\.]+\s)", r"\1", line)
                #logger.debug("Headerless: '" + result)
                state["line"] = result
            #logger.debug("Out line is " + state["line"])
            print(state["line"], file = fOut, end = "")
        
        fIn.close()
        fOut.close()

if __name__ == "__main__":
    main()
