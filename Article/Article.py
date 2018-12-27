'''

@author: Idan
'''

import Utilities
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

#    Article Class    #
     
class Article:
    
    #db = False ==> Reading from api || Db = true ==> Reading from database
    def __init__(self, data, stopWords, db):
        
        
        #Reading from web api
        if(db == False):
            self.title = data['title']
            self.sourceName = data['source']['name']
            self.url = data['url']
            self.content = data['content']
            
            desc = data['description']
            #In case article dosen't include content
            if(self.title is None):
                raise Exception()
            if(self.content is None):
                self.content = " "
            if(desc is None):
                desc = " "
            
                
                
            self.content = self.title + " " + desc + " " + self.content
            
            #TODO: Handle \n in self.content
            #self.content.rstrip("\\r\\n")
            
            
            
            #re.sub(r'\r\n', '', self.content)

            #print(self.content)
            #print("End\n")
            
        #Reading from database
        else:
            self.title  = Utilities.cutOutString("title:", ";sourceName:", data)
            self.sourceName = Utilities.cutOutString("sourceName:", ";url:", data)
            self.url = Utilities.cutOutString("url:", ";content:", data)
            self.content = Utilities.cutOutString("content:", "(.)", data)
        
        
        #Preprocessing article's content
        self.tokens = []
        porter_stemmer = PorterStemmer()
        wordnet_lemmatizer = WordNetLemmatizer()
        #Dividiing content to sentences
        sentences = nltk.sent_tokenize(self.content)
            
        #Dividing each sentence to words
        for sentence in sentences:
            tokenized_sent = nltk.word_tokenize(sentence)
            self.tokens = self.tokens + tokenized_sent
        
        #Stemming and lemmatizing each word
        for word in self.tokens:
            word = porter_stemmer.stem(word)
            word = wordnet_lemmatizer.lemmatize(word)        
        
        self.tokens = list(map(lambda x: x.lower(), self.tokens))
        self.tokens = list(filter(lambda x: x not in stopWords, self.tokens))
        self.tokens = list(filter(lambda x: (x.isalnum()), self.tokens))
        

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