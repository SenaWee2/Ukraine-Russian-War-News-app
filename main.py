import requests
from tkinter import *

def shownews():
    response = requests.get(url,headers=headers).json()
    label.config(text="Headlines: " + response[0]["title"] +"\n"+  "source: " + response[0]["source"]+"\n"+"\n"+
                        "Headlines: " + response[1]["title"] +"\n"+  "source: " + response[1]["source"]+"\n"+"\n"+
                 "Headlines: " + response[2]["title"] +"\n"+  "source: " + response[2]["source"]+"\n"+"\n"+
                 "Headlines: " + response[3]["title"] +"\n"+  "source: " + response[3]["source"]+"\n"+"\n"+
                 "Headlines: " + response[4]["title"] +"\n"+  "source: " + response[4]["source"]+"\n"+"\n"+
                 "Headlines: " + response[5]["title"] +"\n"+  "source: " + response[5]["source"]+"\n"+"\n"+
                 "Headlines: " + response[6]["title"] +"\n"+  "source: " + response[6]["source"]+"\n"+"\n"+
                 "Headlines: " + response[7]["title"] +"\n"+  "source: " + response[7]["source"]+"\n"+"\n"+
                 "Headlines: " + response[8]["title"] +"\n"+  "source: " + response[8]["source"]+"\n"+"\n")


url = "https://ukraine-war-live2.p.rapidapi.com/news"

headers = {
	"X-RapidAPI-Key": "a781a16467mshac78afc027cfb15p11a1b1jsn079a4432bca8",
	"X-RapidAPI-Host": "ukraine-war-live2.p.rapidapi.com"
}

window = Tk()
window.geometry("1200x700")
window.title("Ukraine Russian War News")

button = Button(window,text="Load",font=("BELL MT",30),command=shownews,width=100)
button.pack()

label = Label(window,font=("Arial",12),justify=CENTER) #Use LEFT to organze better
label.pack(pady=20)

window.mainloop()
