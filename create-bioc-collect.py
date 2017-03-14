"""
Create text as collection in BioC format
"""

from glob import glob
from os.path import basename, join

from baleen2.bioc.text import create_bioc_collection_OCC

# pilot abstracts without title
for txt_fname in glob('data/brat/pilot/*abs*.txt'):
    bioc_fname = join('data/bioc/collect/pilot', basename(txt_fname).replace('#brat.txt', '#bioc.xml'))
    bib_fname = join('data', 'bib', '#'.join(basename(txt_fname).split('#')[:2]) + '.bib')
    bib_entry = '\n' + open(bib_fname).read()
    create_bioc_collection_OCC(txt_fname, bioc_fname, part='pilot', with_title=False,
                               doc_infons={'bibtex': bib_entry})

# other abstracts
for part in 'abs1', 'iaa1', 'abs2':
    for txt_fname in glob('data/brat/' + part + '/*abs*.txt'):
        bioc_fname = join('data/bioc/collect/', part, basename(txt_fname).replace('#brat.txt', '#bioc.xml'))
        bib_fname = join('data', 'bib', '#'.join(basename(txt_fname).split('#')[:2]) + '.bib')
        bib_entry = '\n' + open(bib_fname).read()
        create_bioc_collection_OCC(txt_fname, bioc_fname, part=part, doc_infons={'bibtex': bib_entry})

# full text without title
for txt_fname in glob('data/brat/full1/*full*.txt'):
    bioc_fname = join('data/bioc/collect/full1', basename(txt_fname).replace('#brat.txt', '#bioc.xml'))
    bib_fname = join('data', 'bib', '#'.join(basename(txt_fname).split('#')[:2]) + '.bib')
    bib_entry = '\n' + open(bib_fname).read()
    create_bioc_collection_OCC(txt_fname, bioc_fname, part='full1', with_title=False, doc_infons={'bibtex': bib_entry})
