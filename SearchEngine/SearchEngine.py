'''
Created on Dec 25, 2018

@author: Idan
'''
import math
import Utilities
class SearchEngine:
    
    
    def __init__(self, newsClusters):
        self.newsClusters = newsClusters
        self.idf = self.newsClusters.getIDF()
        
        
        
        
        
    def search(self, query):
        
        queryVec = self.createQueryVector(query)
        if(queryVec == None):
            print("No results were found in database")
            return
        
        sims = []
        for centroid in self.newsClusters.getCentroids():
            sims.append(Utilities.cosineSimilarity(centroid, queryVec))
        
        result = self.newsClusters.getClusters()[sims.index(max(sims))]
        result = self.rankResults(result, queryVec)
        
        self.printSearchResult(result)
        
        
        
        
    def createQueryVector(self, query):
        vec = []
        tokens = query.split()
        tokens = list(map(lambda x: x.lower(), tokens)) 
        for word in self.idf:
            #Calculating term weight(tf)
            termFreq = tokens.count(word)
            if(termFreq > 0):
                termWeight = 1 + math.log10(termFreq)
            else:
                termWeight = 0
            
            #Adding tf-idf weight to vector
            vec.append(termWeight * self.idf[word])
            
        isZero = True
        for val in vec:
            if(val != 0):
                isZero = False
        if(isZero):
            return None
            
        return vec
    
    def rankResults(self, result, queryVec):
        rankedResult = []
        for point in result:
            rankedResult.append((point, Utilities.cosineSimilarity(point.getVector(), queryVec)))
        rankedResult.sort(key = self.sortSecond, reverse = True)
        
        return rankedResult
    
    def sortSecond(self, rankedResult):
        return rankedResult[1]
    
    
    def printSearchResult(self, result):
        i=1
        for res in result:
                print("#{0}: {1}; {2}%".format(i, str(res[0]), "%.2f" % (res[1] * 100)))
                i+=1
                