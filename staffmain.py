from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import os

from main import Main
from staff import staff
from staffattendance import Attendance
from stafffacerecognition import Face_Recognition
from staffmaskdetector import Mask_Recognition
from stafftrain import Train
from staffupdatedb import Updatedb



class Face_Recognition_System:
    def __init__(self,root):

        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("SpyCrop Dashboard")
        self.root.configure(bg='#101820')
        root.state('zoomed')   

        img=Image.open(r"img\staffmain.jpg")
        img=img.resize((width, height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-2,y=-2,width=width,height=height)
        

        style = Style()
        style.configure('TButton', font = ('calibri', 20,), borderwidth = '4')

        exitbtn = tkinter.Button(root, text = 'HOME',command=self.mainwindow, activebackground='#121212', activeforeground="#ffffff",bd=0, bg='#121212', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        exitbtn.place(x=100,y=15,height=100,width=130)

        b5 = tkinter.Button(root, text = 'Update Web Portals',command=self.updatesql,activebackground='#101820',activeforeground="#ffffff"   , bg='#101820', fg="#ffffff",bd=0, relief=FLAT, font=("calibri", 15))
        b5.place(x=555,y=105,height=100,width=200)

        b1 = tkinter.Button(root, text = 'staff Details',command=self.staff_details, activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        b1.place(x=400,y=290,height=100,width=200)

        b2 = tkinter.Button(root, text = 'Face Detector',command=self.face_data, bg='#101820', activeforeground="#ffffff", activebackground='#101820',bd=0, fg="#ffffff", relief=FLAT, font=("calibri", 15))
        b2.place(x=400,y=475,height=100,width=200)

        b3 = tkinter.Button(root, text = 'Attendance',command=self.attn, bg='#101820', fg="#ffffff", activeforeground="#ffffff"   , activebackground='#101820',bd=0, relief=FLAT, font=("calibri", 15))
        b3.place(x=695,y=290,height=100,width=200)

        b4 = tkinter.Button(root, text = 'Mask Detector',command=self.mask_detector,bd=0,activebackground='#101820',activeforeground="#ffffff"   , bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        b4.place(x=695,y=475,height=100,width=200)

        b6 = tkinter.Button(root, text = 'Train AI',command=self.train_data,bd=0,activebackground='#101820',activeforeground="#ffffff"   , bg='#101820', fg="#ffffff", relief=FLAT, font=("calibri", 15))
        b6.place(x=550,y=660,height=100,width=200)

        

        # Function Buttons

    def staff_details(self):
        self.new_window=(self.root)
        self.app=staff(self.new_window)

    def open_img(self):
        os.startfile("staffdata")

    def train_data(self):
        self.new_window=(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=(self.root)
        self.app=Face_Recognition(self.new_window)

    def attn(self):
        self.new_window=(self.root)
        self.app=Attendance(self.new_window)

    def updatesql(self):
        self.new_window=(self.root)
        self.app=Updatedb(self.new_window)

    def mask_detector(self):
        self.new_window=(self.root)
        self.app=Mask_Recognition(self.new_window)

    def mainwindow(self):
        self.new_window=(self.root)
        self.app=Main(self.new_window)

    


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
