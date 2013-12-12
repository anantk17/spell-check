import sys
import string
from classes.dictionary import Dictionary
from classes.text import Text


outputfile = ""
if len(sys.argv) == 4 : 
  filedict,filetext,outputfile = sys.argv[1],sys.argv[2],sys.argv[3]
else:
  filedict,filetext = sys.argv[1],sys.argv[2]

d = Dictionary(filedict)
#d.read()
#d.write()
if not outputfile:
  t = Text(filetext)
else:
  t = Text(filetext,outputfile)
#t.write()
#t.chk_words = map(check,
t.chk_words = d.verify(t.chk_words)
t.write()


