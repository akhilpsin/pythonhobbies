#import tkinter module , its an gui library for python
import Tkinter
#import pytube to use youtube methods
from pytube import YouTube
#create an instance of gui window
root=Tk()
#set window size
root.geometry("400x350")
#set window title
root.title("Youtube downloader")

def download():
	try:
		myVar.set("downloading")
		root.update()
		YouTube(link.get()).streams.first().download()
		link.set("operation successful")
	except Exception as e:
		myVar.set("error")
		root.update()
		link.set("enter correct link")

Label(root,text="welcome to downloader",font="Consolas 15 bold").pack()
myVar=StringVar()
myVar.Set("Enter the link below")
Entry(root,textvariable=myVar,width=40).pack(pady=10)
link=StringVar()
Entry(root,textvariable=link,width=40).pack(pady=10)
Button(root,text="Download",command=download).pack()
root.mainloop()
