'''
Created on Dec 7, 2018

@author: Idan
'''
#from Language import Language
import Article
from urllib import request 
import re

#This function cuts out a string between two given sub-strings
def cutOutString(start, end, content):
    startIndex = content.index(start) + len(start)
    endIndex = content.index(end)
    return content[startIndex:endIndex]

#This function streams news from web api
def streamNews(language):
    streamedNews = []
    for sourceName in language.getSources():
        link = 'http://newsapi.org/v2/top-headlines?sources={0}&apiKey=c351e7c333d74c3ca1d882732176a67e'.format(sourceName)
        get = request.urlopen(link)     #Getting articles data

        data = get.read()
        data = data.decode('UTF-8')

        content = re.findall(r'{"source":(.*?)chars]"', data)

        for article in content:             #Creating articles list
            streamedNews.append(Article.Article(article, language.getStopWords(), False))
    return streamedNews        

#This function merges newly streamed news to news database
def addToDB(language, streamedNews):
    for newArticle in streamedNews:
        flag = True
        for oldArticle in language.getArticles():
            if (newArticle == oldArticle):         #Checking if article already exists in database
                flag = False
            
        if(flag == True):
            writeToDB(language.getPath(), newArticle)   #Adding article to database
            language.getArticles().append(newArticle)
                


#This Function adds a new article to database
def writeToDB(path, newArticle):
    #Finding the last line of the file
    langFile = open(path, "r+")
    line = langFile.readline().rstrip()
    while (line != "Articles{"):
        line = langFile.readline().rstrip()
    while (line != "}"):
        line = langFile.readline().rstrip()
    langFile.seek(langFile.tell() - 1, 0)
    
    #Writing out the new object
    langFile.write("title:" + newArticle.getTitle() + ";sourceName:" + newArticle.getSourceName() + ";url:" + newArticle.getUrl() + ";content:" + newArticle.getContent() + "(.)\n}")
    langFile.close()
    
    


#This functions calculates a cluster's mean vector
def getMeanVector(cluster, allWords):
    meanVector = []
    vectors = []
    #Getting vectors from all points in a given cluster
    for point in cluster:
        vectors.append(point.getVector())
        
    #Initializing mean vector for vector addition
    for i in range(len(allWords)):
        meanVector.append(0)
    
    #Adding all vector coordinates
    for vector in vectors:
        meanVector = addVectors(meanVector, vector)
    
    #Dividing each coordinate in mean vector by the amount of vectors    
    for coordinate in meanVector:
        coordinate = coordinate / len(cluster)
        
    return meanVector
    
#This function implements vector addition
def addVectors(vec1, vec2):
    vec = []
    for i in range(len(vec1)):
        vec.append(vec1[i] + vec2[i])
    return vec
    
#This function checks if centroids represented by vectors have changed
def hasChanged(oldCentroids, newCentroids):
    for i in range(len(oldCentroids)):
        if(oldCentroids[i] != newCentroids[i]):
            return True
    return False
        
            
    