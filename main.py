import sys
from classes.dictionary import Dictionary

filename = sys.argv[1]
print filename
d = Dictionary(filename)
d.read()
d.write()