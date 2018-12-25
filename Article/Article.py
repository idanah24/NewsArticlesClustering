'''

@author: Idan
'''

import Utilities
import re

#    Article Class    #
     
class Article:
    
    #db = False ==> Reading from api || Db = true ==> Reading from database
    def __init__(self, data, stopWords, db):
        
        
        #Reading from web api
        if(db == False):
            self.title = Utilities.cutOutString("\"title\":\"", "\",\"description\"", data)
            self.sourceName = Utilities.cutOutString(",\"name\":",  "\"},\"author\"", data)
            self.url = Utilities.cutOutString(",\"url\":", "\",\"urlToImage", data)
            self.content = self.title + " " + Utilities.cutOutString(",\"description\":", "\",\"url", data) + " " + Utilities.cutOutString(",\"content\":", "}", data)
        
        #Reading from database
        else:
            self.title  = Utilities.cutOutString("title:", ";sourceName:", data)
            self.sourceName = Utilities.cutOutString("sourceName:", ";url:", data)
            self.url = Utilities.cutOutString("url:", ";content:", data)
            self.content = Utilities.cutOutString("content:", "(.)", data)
        
        
        #Preprocessing article's content
        self.tokens = self.content.split()
        
        if(db ==  False):
            self.tokens = list(filter(lambda x: (x.isalnum()), self.tokens))    #Removing alphanumerical words
            self.tokens = list(map(lambda x: x.lower(), self.tokens))           #Shifting all words to lower-case only
            self.tokens = list(filter(lambda x: x not in stopWords, self.tokens))   #Removing stopwords
       
        

    #This method counts occourances of a given word
    def countOccourance(self, word):
        return self.getTokens().count(word)
            
    #This operator checks if two articles are the same
    def __eq__(self, other):
        return self.title == other.getTitle()
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title 
    
    def __hash__(self):
        return hash(repr(self))
        
    def getTitle(self):
        return self.title
    def getSourceName(self):
        return self.sourceName
    def getUrl(self):
        return self.url
    def getContent(self):
        return self.content
    def getTokens(self):
        return self.tokens