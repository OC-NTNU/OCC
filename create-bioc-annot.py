"""
Combine Brat text and annotations as collection in BioC format
"""

from glob import glob
from os.path import basename, join

from baleen2.bioc.brat import convert_brat_to_bioc


for part in 'pilot', 'abs1', 'full1':
    bioc_fnames = sorted(glob('data/bioc/collect/' + part + '/*.xml'))
    ann_fnames = sorted(glob('data/brat/' + part + '/*.ann'))

    for bioc_fname, ann_fname in zip(bioc_fnames, ann_fnames):
        bioc_ann_fname = join('data/bioc/annot/', part, basename(bioc_fname)[:-4] + '#annot.xml')
        convert_brat_to_bioc(bioc_fname, ann_fname, bioc_ann_fname)

