"""
get bibtex entries from Crossref for all Brat annotations
"""


import sys
import requests

from os import listdir
from os.path import exists, join


def request_doi_metadata(doi, attempts=10):
    """
    Request metadata for DOI from CrossRef
    """
    headers = {'Accept': 'application/x-bibtex'}

    for i in range(attempts):
        response = requests.get('http://dx.doi.org/{}'.format(doi),
                                headers=headers)
        if response.ok:
            break
    else:
        sys.stderr.write('request for metadata of DOI {} returned {}: {}\n'.format(
            doi, response.status_code, response.reason))
        return {}

    sys.stderr.write('request for metadata of DOI {} succeeded\n'.format(doi))
    return response.text


def get_bibtex_entries(in_dir, bib_dir):
    for path in listdir(in_dir):
        try:
            part1, part2 = path.split('#')[:2]
        except:
            sys.stderr.write('ignoring ' + path + '\n')
            continue

        bib_fname = join(bib_dir, '{}#{}.bib'.format(part1, part2))

        if not exists(bib_fname):
            doi = '/'.join(path.split('#')[:2])
            bib_entry = request_doi_metadata(doi)
            sys.stderr.write('saving ' + bib_fname + '\n')
            with open(bib_fname, 'w') as f:
                f.write(bib_entry)


for part in 'pilot', 'abs1', 'abs2', 'iaa1', 'full1':
    get_bibtex_entries('data/brat/' + part, 'data/bib')
