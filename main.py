
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import os

videosrc = 1

class Main:
    def __init__(self,root):

        width= root.winfo_screenwidth()
        height= root.winfo_screenheight() 
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("SpyCrop Dashboard")
        self.root.configure(bg='black')
        root.state('zoomed')   
        

        img=Image.open(r"img\main.jpg")
        img=img.resize((width, height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-2,y=-3,width=width,height=height)

        style = Style()
        style.configure('TButton', font = ('calibri', 20,), borderwidth = '4')

        exitbtn = tkinter.Button(root, text = 'HOME',command=root.destroy, activebackground='#121212', activeforeground="#ffffff",bd=0, bg='#121212', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        exitbtn.place(x=100,y=25,height=100,width=80)

        b1 = tkinter.Button(root, text = 'Student Management Portal',command=self.studentportal, activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        b1.place(x=260,y=333,height=100,width=576)

        b2 = tkinter.Button(root, text = 'Staff Management Portal',command=self.staffportal, bg='#101820', activeforeground="#ffffff", activebackground='#101820',bd=0, fg="#ffffff", border= 10 , relief=FLAT, font=("calibri", 15))
        b2.place(x=260,y=487,height=100,width=576)

        b2 = tkinter.Button(root, text = 'Mail Servers',command=self.mailservers, bg='#101820', activeforeground="#ffffff", activebackground='#101820',bd=0, fg="#ffffff", border= 10 , relief=FLAT, font=("calibri", 15))
        b2.place(x=260,y=645,height=100,width=576)

    def studentportal(self):
        from studentmain import Face_Recognition_System
        self.new_window=(self.root)
        self.app=Face_Recognition_System(self.new_window)

    def staffportal(self):
        from staffmain import Face_Recognition_System
        self.new_window=(self.root)
        self.app=Face_Recognition_System(self.new_window)

    def mailservers(self):
        from mail import Main
        self.new_window=(self.root)
        self.app=Main(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()

