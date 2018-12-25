'''
Created on Dec 7, 2018

@author: Idan
'''


# -*- coding: utf-8 -*-
import random
import math
from Point import Point
import Utilities


class NewsClusters:
    #This class creates news clusters using the k-means algorithm#
    
    def __init__(self, articles, k):
        self.centroids = []
        self.clusters = []
        
        maxIterations = 10
        self.iterations = 0
        self.change = True

            
        #Creating idf dictionary
        self.idf = self.createIDF(articles)
        
        #Initializing points and their vectors
        self.points = []
        for article in articles:
            self.points.append(Point(article, self.idf))
        
        #K-means algorithm
        #First Step: Generating random centroids
        self.centroids = self.getRandomCentroids(k)
        
        while(self.iterations < maxIterations and self.change == True):
            #Looping while maximum number of iterations hasn't been reached or centroids were not changed
            self.resetClusters(k)
            self.assignToClusters()
            
            #This part handles a case where there is an empty cluster
            if(self.existsEmptyCluster() == True):
                while(self.existsEmptyCluster() == True):
                    self.handleEmptyCluster()
                    
            self.reCalibrateCentroids()
            self.iterations += 1
    


    
    #This method creates the idf dictionary for use
    def createIDF(self, articles):
        #First creating a set of all words in dataset
        allWords = []
        for article in articles:
            for word in article.getTokens():
                allWords.append(word)
                
        allWords = set(allWords)
        idf = dict()
        
        #Creating a dictionary where idf[term] = idf-score
        for word in allWords:
            idf[word] = 0
        
        for word in allWords:
            for article in articles:
                if(word in article.getTokens()):
                    idf[word] += 1
            idf[word] = math.log10((len(articles)/(idf[word])))
        
        #Finding average idf score    
        avgScore = 0
        for word in idf:
            avgScore += idf[word]
        avgScore = avgScore / len(idf)
        
        #Filtering out words with idf score below average
        delWords = set()
        for word in idf:
            if idf[word] < (avgScore / 2):
                delWords.add(word)
        for word in delWords:
            idf.pop(word)
            
        return idf
    
    
    #This method creates and returns a list of randomly selected centroids represented by their vectors
    def getRandomCentroids(self, k):
        centroids = []
        indexes = set()
        while len(centroids) != k:
            i = random.randint(0, len(self.points) - 1)
            if i  not in indexes:
                centroids.append(self.points[i].getVector())
                indexes.add(i)
        return centroids
    
    
    #This method assigns points to their most similar centroids
    def assignToClusters(self):
        
        for point in self.points:
            sims = []
            for centroid in self.centroids:
                sims.append(point.calcSimilarity(centroid))
                    
            self.clusters[sims.index(max(sims))].append(point)   #Assigning to a cluster where the centroid has maximum similarity
            
            point.setSimilarity(max(sims))
            point.setCentroid(self.centroids[sims.index(max(sims))])
    
    
    
    #This method is 
    def reCalibrateCentroids(self):
        newCentroids = []
        
        #Calculating mean vector for each cluster
        for cluster in self.clusters:
            newCentroids.append(Utilities.getMeanVector(cluster, self.idf))
            
        #Checking if centroids have changed
        self.change = Utilities.hasChanged(self.centroids, newCentroids)
        
        #Setting new centroids
        self.centroids = newCentroids
    
    
    
    #This method initializes cluster's list    
    def resetClusters(self, k):
        del self.clusters
        self.clusters = []
        i = 0
        while i<k:
            self.clusters.append([])
            i+=1
    
    #The following 3 methods are handling the empty cluster case
    
    #This method checks if there is an empty cluster after points assigned
    def existsEmptyCluster(self):
        for cluster in self.clusters:
            if (len(cluster) == 0):
                return True
        return False
    
    #This method handles the case of an empty cluster by assigning new random centroid            
    def handleEmptyCluster(self):
        for cluster in self.clusters:
            if(len(cluster) == 0):
                self.centroids[self.clusters.index(cluster)] = self.generateRandomCentroid()
        self.assignToClusters()
    
    #This method returns a vector of a point who isn't a centroid
    def generateRandomCentroid(self):
        for point in self.points:
            if point.getVector() not in self.centroids:
                return point.getVector()
            
            
    #This method prints out clusters
    def printClusters(self):
        i = 1
        for cluster in self.getClusters():
            print('Cluster #{0}'.format(i))
            for point in cluster:
                print(str(point))
            i += 1
            print()    
    
        
    #The following are class getters      
    def getCentroids(self):
        return self.centroids
    def getClusters(self):
        return self.clusters
    def getIterations(self):
        return self.iterations
    def getPoints(self):
        return self.points
    def getIDF(self):
        return self.idf
