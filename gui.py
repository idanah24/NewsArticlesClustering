# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from Language.Language import *
from Article.Article import *


#creates languages and store them in an array
lang = [Language("English")]
#lang+=[Language("Hebrow")]


#asking user to pick a lang and store it in pickLang
print("Pick a language")
for i in range(len(lang)):
    print(str(i+1)+" for "+lang[i].name)
    
pickedLang= input()

#checking the lang input validation
while pickedLang<'0' or pickedLang>'9' or int(pickedLang) > len(lang):
    print(str(pickedLang)+" is invalid input try again")
    pickedLang= input()

pickedLang = lang[int (pickedLang ) -1]


######################################


#num of stored articles 
numOfStoredArt = len(pickedLang.articles)
print("we have "+str( numOfStoredArt )+" stored "+pickedLang.name+" articles")



#option to stream news for the choosen lang
#put streaming in a func

ans = input("would you like to stream new articles? y/n").lower()

while ans not in ('y','n'):
    ans = input( (str(ans)+" is invalid input try again"))
"""
if ans == 'y':
    pickedLang.streamNews()
    print("now we have "+ len(pickedLang.articles)

"""


numOfStoredArt = len(pickedLang.articles)


numOfClusters = input("Enter num of Cluster")
#checking the lang input validation
while pickedLang<'0' or pickedLang>'9' or int(pickedLang) > len(lang):
    print(str(pickedLang)+" is invalid input try again")
    pickedLang= input()



art = lang.getArticles()


x = input('Enter your name:')










for article in art:
    print(article)

#for article in art:
    #print(article)


#tokenized = []
#for article in articles:                #Creating tokenized articles
 #   tokenized.append(article.split())


#Preprocessing
#for i in range(len(tokenized)):
 #   tokenized[i] = list(filter(lambda x: (x.isalnum()), tokenized[i])) #Removing alphanumerical words
  #  tokenized[i] = list(map(lambda x: x.lower(), tokenized[i]))         #Shifting all words to lower-case only
   # tokenized[i] = list(filter(lambda x: x not in stopwords, tokenized[i]))     #Removing stopwords

#print(tokenized)
