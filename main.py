import sys
import string
from classes.dictionary import Dictionary
from classes.text import Text



def write(t,opf):
  if opf:
    f = open(opf,'w')
  else:
    f = open("output.txt",'w')
  result = ""
  for words in t.chk_words:
    if words == '\r\n':
      result += words
    else:
      result+=words+" "
  f.write(result)
  
outputfile = ""
if len(sys.argv) == 4 : 
  filedict,filetext,outputfile = sys.argv[1],sys.argv[2],sys.argv[3]
else:
  filedict,filetext = sys.argv[1],sys.argv[2]

d = Dictionary(filedict)
#d.read()
#d.write()
t = Text(filetext)
#t.write()
#t.chk_words = map(check,
t.chk_words = d.verify(t.chk_words)
t.write()
write(t,outputfile)

