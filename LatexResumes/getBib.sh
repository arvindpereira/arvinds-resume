#!/bin/sh
# First login to Asimov : http://robotics.usc.edu/publications/admin
# 
# Then download the list of publications for the author using the Bibtex api.
# Arvind's author id is 240 in PubDB
# https://robotics.usc.edu/publications/api/publications/author/240/?format=bib
#
# Next, save the bibtex page as something like arvind_pereira.txt
# Finally, run the command
# ./FixBibtex.py -s arvind_pereira.txt -t arvind_pereira.bib
