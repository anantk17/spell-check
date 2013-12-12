import sys
import string
from classes.dictionary import Dictionary
from classes.text import Text


outputfile = ""
if len(sys.argv) == 4 : 						#if all arguments are provided
  filedict,filetext,outputfile = sys.argv[1],sys.argv[2],sys.argv[3]
else:									#if o/p filename is not provided
  filedict,filetext = sys.argv[1],sys.argv[2]

d = Dictionary(filedict)

if not outputfile:
  t = Text(filetext)
else:
  t = Text(filetext,outputfile)

t.chk_words = d.verify(t.chk_words)
t.write()


