#!/bin/bash
####
# Copyright 2021 Nokia
# Licensed under the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
####
# A simple script to convert md files of a directory to rst.
# Pre-requisits:
#  - pandoc
#
# Usage:
# md-to-rst.sh DIR-NAME

if [ -z $1 ]; then echo "Directory is a mandatory parameter."; fi

if ! command -v pandoc &> /dev/null
then
    echo "pandoc is needed to run this script. Please install it."
    exit 1;
fi
if [ ! -d $1 ]
then
    echo "Directory $1 does not exist." 
    exit 1;
fi

for filename in $1/*mod.md; do
    [ -e "$filename" ] || continue
    echo "Converting $filename."
    pandoc -f gfm $filename --from gfm --to rst -s -o ${filename//\-mod\.md/\.rst}
done



