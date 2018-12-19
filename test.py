# -*- coding: utf-8 -*-
from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB
from Evaluation import Evaluation  
import os

lang = Language("C:\English.txt")
#lang = Language("C:\Hebrew.txt")

streamedNews = streamNews(lang)
#addToDB(lang, streamedNews)

articles = lang.getArticles()


news = NewsClusters(streamedNews, 5)
news.printClusters()

eval = Evaluation(news)
eval.createResult()


#TODO: 