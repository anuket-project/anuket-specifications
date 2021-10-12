#!/bin/bash
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

for filename in $1/*.md; do
    [ -e "$filename" ] || continue
    echo "Converting $filename."
    pandoc -f gfm $filename --from markdown --to rst -s -o ${filename%.md}.rst
done


