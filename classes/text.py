#Class to handle text input and output
class Text:
  fileName = ""
  opf = ""
  words = []
  chk_words = []
  
  #Constructor
  def __init__(self,filename,outputfilename="ouput.txt"):   		#if ouputfilename is provided, use it otherwise defualt output file name is "output.txt"
    self.fileName = filename
    self.opf = outputfilename
    self.read()
  
  #Function to read from input file
  def read(self):
    file = open(self.fileName,'r+')
    for line in file:
      self.words.append(line)
    for string in self.words:
      self.chk_words.extend(string.split(' '))
  
  #Function to write to ouput file
  def write(self):
    f = open(self.opf,'w')
    result = ""
    for words in self.chk_words:
      if words == '\r\n':
	result += words
    else:
      result+=words+" "
    f.write(result)
    