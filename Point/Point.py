'''
Created on Dec 7, 2018

@author: Idan
'''
import math

class Point:
    
    def __init__(self, article, idf):
        self.article = article
        self.vector = self.createVector(idf)
        
        self.centroid = None
        self.similarity = 0
        
    
        
        
        
        
        
    #This function calculates the cosine similarity between two given vectors
    def calcSimilarity(self, vec2):
        vec1 = self.getVector()
        dotProduct = 0
        len1 = 0
        len2 = 0
        for i in range(len(vec1)):
            dotProduct += vec1[i] * vec2[i]
            len1 += vec1[i] * vec1[i]
            len2 += vec2[i] * vec2[i]
        len1 = math.sqrt(len1)
        len2 = math.sqrt(len2)
        if (len1 == 0 or len2 == 0):
            return 0
        sim = (dotProduct)/(len1*len2)
        return sim
    
    #This method creates and returns tf-idf vector for the current article
    def createVector(self, idf):
        vec = []
        for word in idf:
            #Calculating term weight(tf)
            termFreq = self.article.getTokens().count(word)
            if(termFreq > 0):
                termWeight = 1 + math.log10(termFreq)
            else:
                termWeight = 0
            
            #Adding tf-idf weight to vector
            vec.append(termWeight * idf[word])
        return vec
    
    def __repr__(self):
        return repr(self.article)
    def __str__(self):
        return repr(self.article)
    
    def getArticle(self):
        return self.article
    def getVector(self):
        return self.vector
    
    def getCentroid(self):
        return self.centroid
    def setCentroid(self, centroid):
        self.centroid = centroid
        
    def getSimilarity(self):
        return self.similarity
    def setSimilarity(self, sim):
        self.similarity = sim