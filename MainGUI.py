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
    
    
    if states[0] and states[1] and states[2]:   #    111

        
        if len(lang.getArticles()) == 0:
            showMessage("No articles to cluster")
        
        elif numOfClusters < 2 or numOfClusters > len(lang.getArticles()) - 1:    #    K should be between 2 and n-1
            showMessage("Wrong number of clusters")
            
        else:
            try:
                stream = streamNews(lang)
            except Exception() as e:
                print(e)
                showMessage("Error while streaming news")

                try:
                    addToDB(lang, stream)
                except Exception() as e:
                    print(e)
                    showMessage("Error while adding to database")
                
            news = NewsClusters(lang.getArticles(), numOfClusters)
            eval = Evaluation(news)
            eval.createResult()
            showMessage("Clustering completed")
        
        
        
    if states[0] and states[1] and not states[2]:   #    110
        try:
            stream = streamNews(lang)
            addToDB(lang, stream)
            showMessage("{0} articles were merged into database".format(len(stream)))
        except Exception() as e:
            print(e)
            showMessage("Error while streaming/adding to database")
    
    
    
    if states[0] and not states[1] and states[2]:       #    101
        try:
            stream = streamNews(lang)
            if numOfClusters < 2 or numOfClusters > len(stream) - 1:
                showMessage("Wrong number of clusters")
            else:
                news = NewsClusters(stream, numOfClusters)
                eval = Evaluation(news)
                eval.createResult()
                showMessage("Clustering completed")
        except Exception() as e:
            print(e)
            showMessage("Error while streaming news")
            

            
    
    if states[0] and not states[1] and not states[2]:       #    100
        showMessage("Please check add to database/cluster boxes")
    
    if not states[0] and states[1] and states[2]:       #    011
        showMessage("Please check 'stream' box first")
    
    if not states[0] and states[1] and not states[2]:       #    010
        showMessage("Please check 'stream' box first")
    
    if not states[0] and not states[1] and states[2]:       #    001
        if numOfClusters < 2 or numOfClusters > len(lang.getArticles()) - 1:
            showMessage("Wrong number of clusters")
        else:
            news = NewsClusters(lang.getArticles(), numOfClusters)
            eval = Evaluation(news)
            eval.createResult()
            showMessage("Clustering completed")
            
    
    if not states[0] and not states[1] and not states[2]:       #    000
        showMessage("Please choose one of the options")
    

def tableGUI():
    langPath=loadGUI()
    try:
        lang = Language(langPath)
    except Exception:
        showMessage("The Chosen file in not a language file , try again")
        
    
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
    numOfCluster.insert(10,"2")

    numOfCluster.place(x=0, y=200, height=20, width=600)

    
    Button(window, text='Quit', command=window.destroy).place(x=0, y=270, height=20, width=600)
    Button(window, text='Submit', command=submit).place(x=0, y=250, height=20, width=600)


    window.mainloop()

def showMessage(msg):
    window = Tk()
    window.resizable(0, 0)
    window.title("Error")
    Label(window, text="").grid()
    mylabel = Label(window, text="  "+msg+"  ")
    mylabel.grid()
    Label(window, text="").grid()
    Button(window, text='Quit', command=window.destroy).grid()
    Label(window, text="").grid()
tableGUI()
