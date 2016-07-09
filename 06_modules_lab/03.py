import os,sys
from os.path import join, getsize

path = '.'
if len(sys.argv) >= 2:
    path = sys.argv[1]

size = 1000000
if len(sys.argv) == 3:
    size = int(sys.argv[2])

for root, dir, files in os.walk(path):
    for name in files:
        if getsize(join(root, name)) > size:
            print "Delete:" , join(root, name),"? [Y/N]"
            if raw_input() == ("Y"):
                os.remove(join(root, name))