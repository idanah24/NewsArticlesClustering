# -*- coding: utf-8 -*-
from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB
from Evaluation import Evaluation

    
    


lang = Language("C:\English.txt")

#streamedNews = streamNews(lang)
#addToDB(lang, streamedNews)

articles = lang.getArticles()

news = NewsClusters(articles, 9)
news.printClusters()

eval = Evaluation(news)
eval.report()
