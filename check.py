
from glob import glob
from os.path import basename, join, exists
from shutil import copyfile

from baleen2.bioc.brat import convert_brat_to_bioc


for part in 'pilot', 'abs1', 'abs2', 'iaa1', 'full1':
    print(80*'-' + '\n' + part + '\n' + 80*'-')
    for ann_fname in glob('data/brat/' + part + '/*.txt'):
        soa_fname = join('data/soa/' + basename(ann_fname).replace('#sent#brat.txt', '.soa'))

        if not exists(soa_fname):#
            src_fname = '/Users/work/Projects/OCEAN-CERTAIN/00_ARCHIVE/_nature/soa/' + basename(soa_fname)
            try:
                copyfile(src_fname, soa_fname)
            except:
                print("Missing: " + soa_fname)
            else:
                print("copied " + soa_fname)
                continue




#         xml_fname = join('data/xml/' +  basename(ann_fname).replace('#sent#brat.txt', '.xml'))
#
#         if not exists(xml_fname):
#             #src_fname = '/Users/work/Projects/OCEAN-CERTAIN/00_ARCHIVE/_nature/sirin/src/' + basename(xml_fname)
#             src_fname = '/Users/work/Projects/OCEAN-CERTAIN/00_ARCHIVE/_nature/abstracts/' + basename(xml_fname)
#             try:
#                 copyfile(src_fname, xml_fname)
#             except:
#                 print("Missing: " + xml_fname)
#             else:
#                 print("copied " + src_fname)
#                 continue
#
#
#             if part != 'pilot':
#                 lines = open(ann_fname).readlines()
#                 s = """<abstract>
# <title>
# {}
# </title>
# <description>
# <p>
# {}</p>
# </description>
# </abstract>
# """.format(lines[0].strip(), ''.join(lines[1:]))
#                 print("Creating: " + xml_fname)
#                 open(xml_fname, 'w').write(s)






        # sent_fname = join('data/sent/' +  basename(ann_fname).replace('#brat', ''))
        #
        # if not exists(sent_fname):
        #     #src_fname = '/Users/work/Projects/OCEAN-CERTAIN/00_ARCHIVE/_nature/sirin/src/' + basename(xml_fname)
        #     try:
        #         copyfile(ann_fname, sent_fname)
        #     except:
        #         print("Missing: " + ann_fname)
        #     else:
        #         print("copied " + ann_fname)
