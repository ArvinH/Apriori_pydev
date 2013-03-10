import string
import re
'''
class Apriori:
   def __init__(self, data, minSup, minConf):
      self.dataset = data
      self.transList = defaultdict(list)
      self.freqList = defaultdict(int)
      self.itemset = set()
      self.highSupportList = list()
      self.numItems = 0
      self.prepData()             # initialize the above collections
      self.F = defaultdict(list)
      self.minSup = minSup
      self.minConf = minConf 
   '''
def getSrcData():
       f = open('../DataSrc/datasrc.txt','r')
       srcdata = []
       Can1 = dict()
       temp = dict()   
       for lines in f:
          lines = lines.strip('\n')
          line = re.split('\W+',lines)
          for item in line:
             if item not in temp:
                temp[item] = 1
             else:
               i = temp[item]
               temp[item] = i+1
               print(temp)
       
       f.close()
       return srcdata

def confidence(self, subCount, itemCount):
         return float(itemCount)/subCount

def support(self, count):
         return float(count)/self.numItems



def main():
   print(getSrcData())
    




if __name__ == '__main__':
    main()
