import csv
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import mysql.connector
from datetime import datetime
from mysql.connector.locales.eng import client_error

class Updatedb:
    mydata=[]
    def __init__(self,root):

        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("SpyCrop Dashboard")
        self.root.configure(bg='#101820')
        root.state('zoomed')

        img = Image.open(r"img\updatedb.jpg")
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-2, y=0, width=2160, height=820)

        b1 = tkinter.Button(root, command=self.updateattndata, text = 'Update Attendance Database.', activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=RIDGE, font=("calibri", 25))
        b1.place(x=60,y=347,height=100,width=475)

        b2 = tkinter.Button(root, command=self.updatealertdata, text = 'Update Alerts Database.', activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=RIDGE, font=("calibri", 25))
        b2.place(x=585,y=347,height=100,width=475)

        exitbtn = tkinter.Button(root, text = 'Back',command=self.main, activebackground='#101820', activeforeground="white",bd=0, bg='#101820', fg="white", relief=FLAT, font=("calibri", 25))
        exitbtn.place(x=60,y=525,height=100,width=970)
        

    def updateattndata(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%y")
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
        with open(f"studentattendance/{date}.csv") as csv_file:
            next(csv_file)
            csvfile = csv.reader(csv_file, delimiter=',')
            all_value = []
            for row in csvfile:
                value = (row[0],row[3],row[4],row[5],row[6]) 
                all_value.append(value)
        
        query = "INSERT INTO `user_attendance` (userid, rollid, datestamp, timestamp, status) VALUES (%s, %s, %s, %s, %s)"

        mycursor = conn.cursor()
        mycursor.executemany(query, all_value)
        conn.commit()

    def updatealertdata(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%y")
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="spycrop")
        with open(f"studentalerts/{date}.csv") as csv_file:
            next(csv_file)
            csvfile = csv.reader(csv_file, delimiter=',')

            all_value = []
            for row in csvfile:
                value = (row[0], row[4], row[5], row[6])
                all_value.append(value)

        query = "INSERT INTO `user_alerts` (id, rollid, datestamp, timestamp) VALUES (%s, %s, %s, %s)"

        mycursor = conn.cursor()
        mycursor.executemany(query, all_value)
        conn.commit()

    def main(self):
        import studentmain
        self.new_window=(self.root)
        self.app=studentmain.Face_Recognition_System(self.new_window)   


if __name__ == "__main__":
    root=Tk()
    obj=Updatedb(root)
    root.mainloop()