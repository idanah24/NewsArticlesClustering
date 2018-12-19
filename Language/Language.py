'''
Created on Dec 7, 2018

@author: Idan
'''


#    Language class    #
# -*- coding: utf-8 -*-
import Article
import os
class Language:
    
    def __init__(self, path):
        
        self.name = os.path.basename(path)
        self.path = path
        self.stopWords = []
        self.sources = []
        self.articles = []
        
        #Loading language from file
        langFile = open(path, "r")
            
        line = langFile.readline().rstrip()
        
        if(line == "Stopwords{"):
            line = langFile.readline().rstrip()
            while(line != "}"):
                self.stopWords.append(line)              #Creating stopwords list
                line = langFile.readline().rstrip()
        line = langFile.readline().rstrip()
        if(line == "Sources{"):
            line = langFile.readline().rstrip()
            while(line != "}"):
                self.sources.append(line)              #Creating sources list
                line = langFile.readline().rstrip()
        line = langFile.readline().rstrip()
        if(line == "Articles{"):
            line = langFile.readline().rstrip()
            while(line != "}"):
                self.articles.append(Article.Article(line, self.stopWords, True))       #Creating articles list
                line = langFile.readline().rstrip()

        langFile.close()
    
    
    #Class getters
    def getPath(self):
        return self.path
    def getStopWords(self):
        return self.stopWords
    def getSources(self):
        return self.sources          
    def getArticles(self):
        return self.articles
