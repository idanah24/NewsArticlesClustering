# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re


stopwords = []
#Loading language from file
lang_file = open("English.txt", "r")
line = lang_file.readline().rstrip()
if(line == "Stopwords{"):
    line = lang_file.readline().rstrip()
    while(line != "}"):
        stopwords.append(line)              #Creating stopwords list
        line = lang_file.readline().rstrip()



#link = 'http://newsapi.org/v2/top-headlines?sources=ynet&apiKey=c351e7c333d74c3ca1d882732176a67e'
link = 'http://newsapi.org/v2/top-headlines?sources=google-news&apiKey=c351e7c333d74c3ca1d882732176a67e'
get = urllib.request.urlopen(link)     #Getting articles data

#data = str(get.read())
data = get.read()
data = data.decode('UTF-8')


#TODO: Improve this part
titles = re.findall(r'"title":"(.*?)",', data)                  #Cutting out titles
descriptions = re.findall(r'"description":"(.*?).","', data)    #Cutting out descriptions
contents = re.findall(r'"content":"(.*?)chars', data)           #Cutting out contents

articles = []
for i in range(min(len(titles), len(descriptions), len(contents))):         #Creating articles list
    articles.append(titles[i] + descriptions[i] + contents[i])

tokenized = []
for article in articles:                #Creating tokenized articles
    tokenized.append(article.split())


#Preprocessing
for i in range(len(tokenized)):
    tokenized[i] = list(filter(lambda x: (x.isalnum()), tokenized[i])) #Removing alphanumerical words
    tokenized[i] = list(map(lambda x: x.lower(), tokenized[i]))         #Shifting all words to lower-case only
    tokenized[i] = list(filter(lambda x: x not in stopwords, tokenized[i]))     #Removing stopwords

print(tokenized)
