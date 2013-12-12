class Text:
  fileName = ""
  words = []
  chk_words = []
  
  def __init__(self,filename):
    self.fileName = filename
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
    print self.words
    print self.chk_words
    