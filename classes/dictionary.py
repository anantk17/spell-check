import string

class Dictionary:
  fileName = ""
  words = []
  hashed_words = []
  
  def __init__(self,filename):
   self.fileName = filename
   self.words = []
   self.hashed_words = []
   self.read()
     
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
    
  def verify(self,t):
    result = []
    for word in t:
      result.append(self.check(word))
    return result
  
  def check(self,w):
    if w.lower() in self.words:
      return w
    elif w.lower()[:-1] in self.words and (w[-1:] in string.punctuation):
      return w
    elif w == '\r\n' or (w[:1] in string.punctuation):
      return w
    else :
      for word in self.words:
	if w.lower()[:-1] == word[:-1]:
	  w = word
	  return w
	elif w.lower()[:-2] == word[:-1] and w.lower()[-1:] in string.punctuation :
	  w = word + w[-1:]
	  return w
	
      return ws 