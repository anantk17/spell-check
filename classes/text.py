class Text:
  fileName = ""
  opf = ""
  words = []
  chk_words = []
  
  def __init__(self,filename,outputfilename="ouput.txt"):
    self.fileName = filename
    self.opf = outputfilename
    self.read()
    
  def read(self):
    file = open(self.fileName,'r+')
    for line in file:
      self.words.append(line)
    #self.chk_words = map(lambda s : s.split('\r\n'),self.words)
    #for string in self.words:
    #  self.chk_words.extend(string.split('\r\n'))
    #self.words = self.chk_words
    #self.chk_words = []
    for string in self.words:
      self.chk_words.extend(string.split(' '))
  
  def write(self):
    f = open(self.opf,'w')
    result = ""
    for words in self.chk_words:
      if words == '\r\n':
	result += words
    else:
      result+=words+" "
    f.write(result)
    