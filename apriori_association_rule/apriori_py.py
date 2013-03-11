import string
import re
class Apriori:
  def __init__(self,filepath, minSup, minConf):
      self.minSup = minSup
      self.minConf = minConf
      self.filepath = filepath
  def getSrcData(self):
         f = open(self.filepath,'r')
         srcdata = []
         for lines in f:
            lines = lines.strip('\n')
            #delete space, tab, comma and numbers
            line = re.split('[^a-zA-Z0-9_]+',lines)
            del line[0:1]
            print(line) 
            srcdata.append(line) 
         f.close()
         return srcdata

  def getC1(self,srcdata):
         c1 = {}
         #in each transaction
         for line in srcdata:
            #for each item in one transaction
            for item in line:
               #put into a set and return a frozenset to be key of dict
               s = set()
               s.add(item)
               key = frozenset(s)
               #if the item has appeared before,plus one 
               if key in c1:
                  c1[key] = c1[key] + 1
               else:
                  c1[key] = 1
         return c1

  def getL(self,Candidate):
     #key in C will be deleted if its support count less than given value
      deleted_key = []
      for key in Candidate:
         Can_sup = Candidate[key]
         if Can_sup < self.minSup:
            deleted_key.append(key)
      #for each key's support count less than given value, then delete
      for key in deleted_key:
         del Candidate[key]
      return Candidate
  # get the next candidate from pre L
  # and scan original dataset
  def getC2(self,preL, srcdata):
      c2 = {}
      # would have some redundant computation...
      for key1 in preL:
         for key2 in preL:
            if key1 != key2:
               key = key1.union(key2)
               c2[key] = 0
      # count each item
      for line in srcdata:
         for item in c2:
            if item.issubset(line):
               c2[item] = c2[item] + 1
      return c2 

  def Apriori_algo(self):
      #get src data
      srcdata = self.getSrcData()
      #get C1
      candidate_set = self.getC1(srcdata)
      L = {}
      Lk = {}
      while True:
         #keep test if there any new L generate, if not, then over.
         TempL = self.getL(candidate_set)
         if not TempL:
            break
         else:
            L = TempL
            #get next candidate from pre L
            candidate_set = self.getC2(L,srcdata)
            Lk.update(L)
      return Lk
  def genAssociation_Rule(self, freq_itemset):
      # find every frequency itemset and count their conf
      for freq_item1 in freq_itemset:
         for freq_item2 in freq_itemset:
            if freq_item1 != freq_item2:
               if freq_item1.issubset(freq_item2):
                  diffset = freq_item2.difference(freq_item1)
                  
                  conf = freq_itemset[diffset]/freq_itemset[freq_item1]
                  if conf >= self.minConf:
                    print(freq_item1,'->',diffset)
def main():
   a = Apriori('../DataSrc/datasrc.txt',0.5,0.66)
   L = a.Apriori_algo()
   print(L)
   a.genAssociation_Rule(L)



if __name__ == '__main__':
    main()
