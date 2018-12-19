from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import filedialog as fd

def loadGUI():
    window = Tk()
    
    window.title("NAC - News Articles Clustering")
    path = fd.askopenfilename()
    window.destroy()
    return path

langPath=loadGUI()




#state: stream , addDB , cluster
def startCluster (numOfClusters,states):

    print(states)


    pickedLang = Language(langPath)

    #num of stored articles 
    numOfStoredArt = len(pickedLang.articles)
    print("we have "+str( numOfStoredArt )+" stored "+pickedLang.name+" articles")


    #option to stream news for the choosen lang
    #put streaming in a func
    if numOfStoredArt == 0:
        print("No stored articles --> exiting...")
        exit
    #complte the streaming procces
    stream = pickedLang.getArticles()
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
        eval.report()
    
    

    
    








def tableGUI():

    def submit():
        startCluster(int(numOfCluster.get()),(stream.get(),addDB.get(),cluster.get()))










    
    window = Tk()

    window.geometry("600x300")
    window.resizable(0, 0)
    window.title("NAC - Loaded News Articles")
    mylabel = Label(window, text="choosen language path : "+langPath)
    mylabel.place(x=0, y=0, height=20, width=600)


    stream = IntVar()
    Checkbutton(window, text="Stream", variable=stream).place(x=0, y=25, height=20, width=600)
    addDB = IntVar()
    Checkbutton(window, text="Add To DataBase", variable=addDB).place(x=0, y=50, height=20, width=600)
    cluster = IntVar()
    Checkbutton(window, text="Cluster", variable=cluster).place(x=0, y=100, height=20, width=600)


    Label(window, text="Last Name").place(x=0, y=180, height=20, width=600)

    numOfCluster = Entry(window)
    numOfCluster.insert(10,"1")

    numOfCluster.place(x=0, y=200, height=20, width=600)

    
    Button(window, text='Quit', command=window.destroy).place(x=0, y=250, height=20, width=600)
    Button(window, text='Submit', command=submit).place(x=0, y=270, height=20, width=600)




    
        
tableGUI()

"""
def mainGUI() :
window = Tk()

window.geometry("800x400")
window.resizable(0, 0)
window.title("NAC - News Articles Clustering")
#window.withdraw()
path = fd.askdirectory()
#path = StringVar()
pathEntered = ttk.Entry(window, width = 70, textvariable = path)
pathEntered.place(x=205, y=150, width=400)

mylabel = Label(window, text="Directory Path")
mylabel.place(x=80, y=150, height=20, width=95)

binsEntered = StringVar()
bins = ttk.Entry(window, width = 40, textvariable = binsEntered)


mylabel2 = Label(window)
mylabel2.place(x=350, y=670, height=20, width=100)
label2Text = StringVar()
mylabel2.configure(textvariable=label2Text)
mylabel2.pack()

mylabel3 = Label(window)
mylabel3.place(x=350, y=550, height=20,width=100)
label3Text = StringVar()
mylabel3.configure(textvariable=label3Text)
mylabel3.pack()

B = Button(window, text = "Browse")
B.place(x = 620, y = 145, width = 100, height = 30)
B.bind("<ButtonPress-1>", lambda event, arg = pathEntered: p.read_file_to_list(arg))

B = Button(window, text = "Summerize")
B.place(x = 350, y = 220, width = 150, height = 25)
B.bind("<ButtonPress-1>", lambda event: p.read_structure())

B = Button(window, text = "Vector")
B.place(x = 350, y = 250, width = 150, height = 25)
B.bind("<ButtonPress-1>", lambda event: v.createVector(p.getWholeFile()))

B = Button(window, text = "simMat")
B.place(x = 350, y = 280, width = 150, height = 25)
B.bind("<ButtonPress-1>", lambda event: sim.createMat(p.getSentences(), v.getSentence_vectors()))




def ranked():
    sim.rank()
    print(sim.getScores())
    ranked_sentences = sorted(((sim.getScores()[i], s) for i, s in enumerate(p.getSentences())), reverse=True)
    for i in range(10):
        print('4*8*84*')
        print(ranked_sentences[i][1])

B = Button(window, text = "final")
B.place(x = 350, y = 310, width = 150, height = 25)
B.bind("<ButtonPress-1>", lambda event: ranked())

"""
