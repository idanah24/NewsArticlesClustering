# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from Language.Language import *
from Article.Article import *


lang = Language("English")

art = lang.getArticles()

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
