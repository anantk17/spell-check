class Dictionary:
  fileName = ""
  words = []
  hashed_words = []
  
  def __init__(self,filename):
   self.fileName = filename
   self.words = []
   self.hashed_words = []
     
  def write(self):
    print self.fileName
    print self.words
  
  def read(self):
    file = open(self.fileName,'r')
    for line in file:
      self.words.append(line)
    self.words = map(lambda s: s.strip(), self.words)
    
  def dhash(self):
    hashed_words = map(hash, words)