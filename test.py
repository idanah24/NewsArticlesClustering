# -*- coding: utf-8 -*-
from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB
from Evaluation import Evaluation  
import os


lang = Language("c:/English.txt")
#lang = Language("C:\Users\Idan\git\NewsArticlesClustering\Language\Hebrew.txt")

streamedNews = streamNews(lang)
addToDB(lang, streamedNews)


articles = lang.getArticles()


news = NewsClusters(articles, 10)
news.printClusters()

eval = Evaluation(news)
eval.createResult()


#TODO: 