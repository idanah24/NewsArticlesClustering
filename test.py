# -*- coding: utf-8 -*-
from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB, otherStreamNews
from Evaluation import Evaluation  
from SearchEngine import SearchEngine
import os
from os.path import dirname
import sys


sys.path.append(dirname(__file__))
sys.path.append(dirname(__file__) + "\\Article")
sys.path.append(dirname(__file__) + "\\Evaluation")
sys.path.append(dirname(__file__) + "\\Language")
sys.path.append(dirname(__file__) + "\\NewsClusters")
sys.path.append(dirname(__file__) + "\\Point")
sys.path.append(dirname(__file__) + "\\SearchEngine")
sys.path.append(dirname(__file__) + "\\Utilities")



#lang = Language("c:/English.txt")
lang = Language("c:/Hebrew.txt")
#lang = Language("C:\Users\Idan\git\NewsArticlesClustering\Language\Hebrew.txt")

#streamedNews = streamNews(lang)
#addToDB(lang, streamedNews)
otherStreamNews(lang)


articles = lang.getArticles()


#news = NewsClusters(streamedNews, 4)
#news.printClusters()

#eval = Evaluation(news)
#eval.createResult()


#engine = SearchEngine(news)


#engine.search("Trump")

#TODO: 