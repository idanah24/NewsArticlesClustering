# -*- coding: utf-8 -*-

import os
from os.path import dirname
import sys
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize


sys.path.append(dirname(__file__))
sys.path.append(dirname(__file__) + "\\Article")
sys.path.append(dirname(__file__) + "\\Evaluation")
sys.path.append(dirname(__file__) + "\\Language")
sys.path.append(dirname(__file__) + "\\NewsClusters")
sys.path.append(dirname(__file__) + "\\Point")
sys.path.append(dirname(__file__) + "\\SearchEngine")
sys.path.append(dirname(__file__) + "\\Utilities")

from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB
from Evaluation import Evaluation  
from SearchEngine import SearchEngine



lang = Language("c:/English.txt")
#lang = Language("c:/Hebrew.txt")
#lang = Language("C:\Users\Idan\git\NewsArticlesClustering\Language\Hebrew.txt")

streamedNews = streamNews(lang)
#addToDB(lang, streamedNews)
#otherStreamNews(lang)
tokens = []
allwords = []
for article in streamedNews:
    #tokens = tokens + article.getTokens()
    tokens.append(article.getTokens())
    allwords = allwords + article.getTokens()

allwords = set(allwords)

data = tokens

tagged_data = []

for i in range(len(streamedNews)):
    tagged_data.append(TaggedDocument(words=tokens[i], tags=str(i+1)))


#tagged_data = [TaggedDocument(words=tokens[i], tags=[str(i)]) for i, _d in enumerate(data)]

max_epochs = 20
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=len(allwords),
                alpha=alpha, 
                min_alpha=0.00025,
                min_count=1,
                dm =1)
  
model.build_vocab(tagged_data)

model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)

#for epoch in range(max_epochs):
    #print('iteration {0}'.format(epoch))
    #model.train(tagged_data,
                #total_examples=model.corpus_count,
                #epochs=model.iter)
    # decrease the learning rate
    #model.alpha -= 0.0002
    # fix the learning rate, no decay
    #model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")





#articles = lang.getArticles()
#print(len(streamedNews))
    


news = NewsClusters(streamedNews, 4)
#news.printClusters()

eval = Evaluation(news)
eval.createResult()
print("done")

#engine = SearchEngine(news)


#engine.search("Trump")

#TODO: 
