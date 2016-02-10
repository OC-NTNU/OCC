#!/usr/bin/env python

"""
quick hack to add empty annotations for a new annotator

run from root dir as

./new_annotator.py XX
"""

import sys
from os import makedirs
from glob import glob
from os.path import basename, splitext
from os import symlink

annotator = sys.argv[1]

annot_dir = 'data/brat/' + annotator

makedirs(annot_dir)

for txt_fname in glob('data/sent/*.txt'):
    root =  annot_dir + '/' + splitext(basename(txt_fname))[0] + '#brat_' + annotator
    symlink('../../sent/' + basename(txt_fname), root + '.txt')
    open(root + '.ann', 'w')





