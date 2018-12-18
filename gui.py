# -*- coding: utf-8 -*-
from NewsClusters import NewsClusters
from Language import Language
from Utilities import streamNews, addToDB
from Evaluation import Evaluation


#creates languages and store them in an array
lang = [Language("English")]
#lang+=[Language("Hebrow")]


#asking user to pick a lang and store it in pickLang
print("Pick a language")
for i in range(len(lang)):
    print(str(i+1)+" for "+lang[i].name)
    
pickedLang= input()

#checking the lang input validation
while not pickedLang.isNumeric() or int(pickedLang) > len(lang):
    print(str(pickedLang)+" is invalid input try again")
    pickedLang= input()

pickedLang = lang[int (pickedLang ) -1]


######################################


#num of stored articles 
numOfStoredArt = len(pickedLang.articles)
print("we have "+str( numOfStoredArt )+" stored "+pickedLang.name+" articles")



#option to stream news for the choosen lang
#put streaming in a func
if numOfStoredArt == 0:
    print("No stored articles --> Streaming ... ")
    pickedLang.streamNews()
    numOfStoredArt = len(pickedLang.articles)


else:    
    ans = input("would you like to stream new articles? y/n").lower()

    while ans not in ('y','n'):
        ans = input( ans+" is invalid input try again")
    
    if ans == 'y':
        pickedLang.streamNews()
        print("now we have "+ len(pickedLang.articles))
        numOfStoredArt = len(pickedLang.articles)

if numOfStoredArt <1:
    print("No articles to cluster \nExiting...")
    exit

numOfClusters = input("Enter num of Cluster")

              
#checking the lang input validation
while not numOfClusters.isNumeric() or int(numOfClusters) > numOfStoredArt:
    if int(numOfClusters) > numOfStoredArt :
        print("pick a number thats less then "+str(numOfStoredArt))
    else:
        print(numOfClusters+" is invalid input try again")
    
    numOfClusters = input()



print("Starting Cluster...")

articles = lang.getArticles()

news = NewsClusters(articles, numOfClusters)
news.printClusters()

eval = Evaluation(news)
eval.report()






