from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import messagebox
import csv
import os
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Attendance Dashboard")
        self.root.configure(bg='#ffffff')
        root.state('zoomed')

        # Text Variables

        self.var_rollid = StringVar()
        self.var_timestamp = StringVar()
        self.var_datestamp = StringVar()
        self.var_attn = StringVar()

        img=Image.open(r"logo\logo_whiteLandscape.jpg")
        img=img.resize((1536,221),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-3,y=0,width=1536,height=221)

        main_frame=tkinter.Frame(bg='white')
        main_frame.place(x=0,y=221,width=1536,height=650)

        exitbtn = tkinter.Button(root, text = 'Back',command=self.main, activebackground='#ffffff', activeforeground="black",bd=0, bg='#ffffff', fg="black", relief=FLAT, font=("calibri", 15))
        exitbtn.place(x=50,y=13,height=30,width=40)

        # Left Title Frame
        left_frame =tkinter.LabelFrame(main_frame,bd=0,relief=RIDGE,font = ('calibri', 20,), text="Attendance Details",bg='white')
        left_frame.place(x=15,y=10,width=768,height=650)

        left_Subframe=tkinter.Frame(left_frame, bg='white', bd=2, relief=RIDGE)
        left_Subframe.place(x=5,y=10,width=635,height=500)

        # Labels and Entry
        Rollid =tkinter.Label(left_Subframe,text= "staff Roll ID", bd=0,relief=RIDGE,font = ('calibri', 15,), bg='white', fg="black")
        Rollid.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        rollID_entry=ttk.Entry(left_Subframe, width=10,textvariable=self.var_rollid,font = ('calibri', 15,))
        rollID_entry.grid(row=1, column=1,padx=10, pady=10, sticky=W)

        studtime =tkinter.Label(left_Subframe,text= "Timestamp", bd=0,relief=RIDGE,font = ('calibri', 15,), bg='white', fg="black")
        studtime.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        studtime_entry=ttk.Entry(left_Subframe, width=10,textvariable=self.var_timestamp,font = ('calibri', 15,))
        studtime_entry.grid(row=2, column=1,padx=10, pady=10, sticky=W)

        studdate =tkinter.Label(left_Subframe,text= "Datestamp", bd=0,relief=RIDGE,font = ('calibri', 15,), bg='white', fg="black")
        studdate.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        studdate_entry=ttk.Entry(left_Subframe, width=10,textvariable=self.var_datestamp, font = ('calibri', 15,))
        studdate_entry.grid(row=3, column=1,padx=10, pady=10, sticky=W)
        
        att_mark=tkinter.Label(left_Subframe, font = ('calibri', 15,), text="Attendence Status",  bg="white")
        att_mark.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        att_combo=ttk.Combobox(left_Subframe,textvariable=self.var_attn, font = ('calibri', 15,), state="readonly")
        att_combo["values"]=("Status", "Present", "Absent")
        att_combo.current(0)
        att_combo.grid(row=4, column=2 , padx=10, pady=10, sticky=W)

        btn_frame = tkinter.Frame(left_Subframe, bd=2, relief=FLAT)
        btn_frame.place(x=0, y=350, width=630, height=45)

        reset_btn=tkinter.Button(btn_frame, text="Reset",width=31,command=self.reset_data, font = ('calibri', 15,), relief=FLAT, bg="white")
        reset_btn.grid(row=0, column=1)


        btn_frame1 = tkinter.Frame(left_Subframe, bd=2, relief=FLAT)
        btn_frame1.place(x=0, y=295, width=630, height=45)

        save_btn=tkinter.Button(btn_frame1, text="Import CSV", command=self.importCSV, width=31, font = ('calibri', 15,), relief=FLAT, bg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn=tkinter.Button(btn_frame1, text="Export CSV", command=self.exportCSV,width=31, font = ('calibri', 15,), relief=FLAT , bg="white")
        update_btn.grid(row=0, column=1)

        # Right Title Frame
        right_frame =tkinter.LabelFrame(main_frame,bd=0,relief=FLAT,font = ('calibri', 20,), text="Attendance Summary",bg='white')
        right_frame.place(x=700,y=10,width=850,height=650)

        right_Subframe=tkinter.Frame(right_frame, bg='white', bd=2, relief=RIDGE)
        right_Subframe.place(x=5,y=10,width=800,height=500)

        scroll_x=ttk.Scrollbar(right_Subframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_Subframe, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(right_Subframe,column=("id", "name","dept","rollno","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable)
        scroll_y.config(command=self.AttendanceReportTable)

        self.AttendanceReportTable.heading("id",text="ID")
        self.AttendanceReportTable.heading("rollno",text="Roll ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dept",text="Department")
        self.AttendanceReportTable.heading("time",text="Timestamp")
        self.AttendanceReportTable.heading("date",text="Datestamp")
        self.AttendanceReportTable.heading("attendance",text="Status")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=50)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dept",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.getCursor)

        # Functions
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir="staffattendance",title="Open CSV", filetypes=(("CSV File",".csv"),("All Files", "*.*")),parent=self.root)
        with open(fln) as myfile:
            next(myfile)
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data Detected", "Please Make Sure the Data Exists", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir="staffattendance",title="Open CSV", filetypes=(("CSV File",".csv"),("All Files", "*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export Successful","Data was Sucessfully Exported. You can view it under attendence/"+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error", f"Couldn't Export Data. Code:{str(es)}", parent=self.root)


    def getCursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_rollid.set(rows[3])
        self.var_datestamp.set(rows[4])
        self.var_timestamp.set(rows[5])
        self.var_attn.set(rows[6])

    def reset_data(self):
        self.var_rollid.set(" ")
        self.var_datestamp.set(" ")
        self.var_timestamp.set(" ")
        self.var_attn.set("Status")

    def main(self):
        import staffmain
        self.new_window=(self.root)
        self.app=staffmain.Face_Recognition_System(self.new_window)





        


if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()