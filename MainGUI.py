# -*- coding: utf-8 -*-

import os
import sys
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import filedialog as fd
import os
from os.path import dirname


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

def loadGUI():
    window = Tk()
    
    window.title("NAC - News Articles Clustering")
    path = fd.askopenfilename()
    window.destroy()
    return path




#state: stream , addDB , cluster
def Action(lang, numOfClusters,states):
    
    
    
    #num of stored articles 
    numOfStoredArt = len(lang.articles)
    if states[0] and states[1] and states[2]:
        stream = streamNews(lang)
        #TODO: Catch urllib exceptions
        addToDB(lang, stream)
        news = NewsClusters(lang.getArticles(), numOfStoredArt)
        eval = Evaluation(news)
        eval.createResult()
        showMessage("{0} Articles were merged into database\nClustering completed!".format(len(stream)))





    #option to stream news for the choosen lang
    #put streaming in a func
    if numOfStoredArt == 0:
        showMessage("No stored articles")
        
    #complte the streaming procces
    stream = lang.getArticles()
    if states[0]:
        stream = streamNews(pickedLang)
        if states[1]:
            addToDB(pickedLang,stream)
    if states[2]:
        if numOfStoredArt <numOfClusters or numOfStoredArt <1:
            print("invalid input")
            exit
            
        news = NewsClusters(stream , numOfClusters)
        news.printClusters()
        eval = Evaluation(news)
        eval.createResult()
    
    

    
    








def tableGUI():
    langPath=loadGUI()
    lang = Language(langPath)
    
    def submit():
        Action(lang, int(numOfCluster.get()),(stream.get(),addDB.get(),cluster.get()))

    window = Tk()
    
    window.geometry("600x300")
    window.resizable(0, 0)
    window.title("NAC - Loaded News Articles")
    mylabel = Label(window, text="Chosen language path :")
    mylabel.place(x=0, y=0, height=20, width=600)
    #Test
    mylabel = Label(window, text="Current stored articles : {0}".format(len(lang.getArticles())))
    mylabel.place(x=0, y=40, height=20, width=600)
    Label(window, text=langPath).place(x=0, y=20, height=20, width=600)


    stream = IntVar()
    Checkbutton(window, text="Stream", variable=stream).place(x=0, y=60, height=20, width=600)
    addDB = IntVar()
    Checkbutton(window, text="Add To DataBase", variable=addDB).place(x=0, y=80, height=20, width=600)
    cluster = IntVar()
    Checkbutton(window, text="Cluster", variable=cluster).place(x=0, y=100, height=20, width=600)


    Label(window, text="Number of clusters:").place(x=0, y=180, height=20, width=600)

    numOfCluster = Entry(window)
    numOfCluster.insert(10,"1")

    numOfCluster.place(x=0, y=200, height=20, width=600)

    
    Button(window, text='Quit', command=window.destroy).place(x=0, y=270, height=20, width=600)
    Button(window, text='Submit', command=submit).place(x=0, y=250, height=20, width=600)


    window.mainloop()

def showMessage(msg):
    window = Tk()
    window.geometry("200x100")
    window.resizable(0, 0)
    window.title("Error")
    mylabel = Label(window, text=msg)
    mylabel.place(x=0, y=20, height=20, width=200)
    Button(window, text='Quit', command=window.destroy).place(x=0, y=60, height=20, width=200)
tableGUI()