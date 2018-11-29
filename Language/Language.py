#    Language class    #
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from Article.Article import *
class Language:
    
    def __init__(self, fileName):
        self.name = fileName
        self.stopWords = []
        self.sources = []
        self.articles = []
        
        #Loading language from file
        langFile = open("Language\\" + fileName + ".txt", "r")
            
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
                
        #Reading articles from web
        for sourceName in self.sources:
            link = 'http://newsapi.org/v2/top-headlines?sources={0}&apiKey=c351e7c333d74c3ca1d882732176a67e'.format(sourceName)
            get = urllib.request.urlopen(link)     #Getting articles data

            data = get.read()
            data = data.decode('UTF-8')

            content = re.findall(r'{"source":(.*?)chars]"', data)

            for article in content:             #Creating articles list
                self.articles.append(Article(article))

    
    def getName(self):
        return self.name
    def getStopWords(self):
        return self.stopWords
    def getSources(self):
        return self.sources          
    def getArticles(self):
        return self.articles
