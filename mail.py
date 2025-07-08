import sys
import os
from tkinter import *
from threading import Thread


from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import os


class Main:
    def __init__(self,root):

        width= root.winfo_screenwidth()
        height= root.winfo_screenheight() 
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("SpyCrop Dashboard")
        self.root.configure(bg='black')
        root.state('zoomed')   

        
        img=Image.open(r"img\mailserver.jpg")
        img=img.resize((width, height),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-2,y=-3,width=width,height=height)

        style = Style()
        style.configure('TButton', font = ('calibri', 20,), borderwidth = '4')

        exitbtn = tkinter.Button(root, text = 'BACK',command=self.mainwindow, activebackground='#121212', activeforeground="#ffffff",bd=0, bg='#121212', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        exitbtn.place(x=100,y=17,height=100,width=80)

        btn = tkinter.Button(text = 'Start Student Mail Server',command=self.server0, activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        btn.place(x=290,y=382,height=100,width=400)

        btn = tkinter.Button(text = 'Start Staff Mail Server',command=self.server1, activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        btn.place(x=290,y=580,height=100,width=400)

    def mainwindow(self):
        from main import Main
        self.new_window=(self.root)
        self.app=Main(self.new_window)

    def server0(self):
            t = Thread(target = lambda: os.system('python studentstartmailserver.py'))
            t.start()

    def server1(self):
            t = Thread(target = lambda: os.system('python staffstartmailserver.py'))
            t.start()        

if __name__ == "__main__":  
    root=Tk()
    obj=Main(root)
    root.mainloop()
