import string
import re
def getSrcData():
    f = open('../DataSrc/datasrc.txt','r')
    srcdata = []
    for lines in f:
        line = re.split('\W+',lines)
        srcdata.append(line)
        
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