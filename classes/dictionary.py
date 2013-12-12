import string

#Class to handle dictionary operations
class Dictionary:
  fileName = ""
  words = []
  hashed_words = []
  
  #Constructor
  def __init__(self,filename):
   self.fileName = filename
   self.words = []
   self.hashed_words = []
   self.read()
  
  #Function to open input file and read text from it
  def read(self):
    file = open(self.fileName,'r')
    for line in file:
      self.words.append(line)
    self.words = map(lambda s: s.strip(), self.words)
  
  #Function to hash the strings found in input text
  def dhash(self):
    hashed_words = map(hash, words)
  
  #Function called for spell-checking
  def verify(self,t):
    result = []
    for word in t:
      result.append(self.check(word))
    return result
  
  #Function that actually performs spell check
  def check(self,w):
    if w.lower() in self.words:	
      return w									#if word is present in dictionary return it
    elif w.lower()[:-1] in self.words and (w[-1:] in string.punctuation):
      return w									#if word contains punctuation check if remainder of word is in dictionary
    elif w == '\r\n' or (w[:1] in string.punctuation):
      return w									#if word contains EOF characters or punctuation marks only, return them as is
    else :
      for word in self.words:							#word is not present in dictionary as is
	if w.lower()[:-1] == word[:-1]:
	  w = word								#if last character is different replace word with the closest match in dictionary
	  return w
	elif w.lower()[:-2] == word[:-1] and w.lower()[-1:] in string.punctuation :
	  w = word + w[-1:]							#if last character is a punctuation mark, check for above condition on the second last character
	  return w
	
      return w									#if word is not in dictionary in any form, return the word as is