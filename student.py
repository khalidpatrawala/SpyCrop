from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
import cv2
from mysql.connector.locales.eng import client_error

videosrc = 1  # 3 - MI Camera / 0 - PC Camera  / 1 - DroidCam

class Student:
    def __init__(self,root):
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Attendance Dashboard")
        self.root.configure(bg='#ffffff')
        root.state('zoomed')    

        # Variables
        self.var_id=StringVar()
        self.var_dept=StringVar()
        self.var_sem=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_roll=StringVar()
        self.var_enroll=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()

        img=Image.open(r"logo\logo_whiteLandscape.jpg")
        img=img.resize((1536,221),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-3,y=0,width=1536,height=221)

        main_frame=tkinter.Frame(bg='white')
        main_frame.place(x=0,y=221,width=width,height=height)

        exitbtn = tkinter.Button(root, text = 'Back',command=self.main, activebackground='#ffffff', activeforeground="black",bd=0, bg='#ffffff', fg="black", relief=FLAT, font=("calibri", 15))
        exitbtn.place(x=50,y=13,height=30,width=40)

        # Left Title Frame
        left_frame =tkinter.LabelFrame(main_frame,bd=0,relief=RIDGE,font = ('calibri', 20,), text=" Student Details",bg='white')
        left_frame.place(x=15,y=10,width=768,height=750)

        dept_label=tkinter.Label(left_frame, font = ('calibri', 15,), text="Department", bg="white", fg="black")
        dept_label.grid(row=0,column=0, padx=10)
        dept_combo=ttk.Combobox(left_frame, textvariable=self.var_dept, font = ('calibri', 15,), state="readonly")
        dept_combo["values"]=("Select Department", "INFT", "EJ", "COEN")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=20, pady=30, sticky=W)

        dept_label=tkinter.Label(left_frame, font = ('calibri', 15,), text="Semester",  bg="white")
        dept_label.grid(row=0,column=2)
        dept_combo=ttk.Combobox(left_frame, textvariable=self.var_sem, font = ('calibri', 15,), state="readonly")
        dept_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=3, padx=20, pady=30, sticky=W)

        # SubFrame Left Main Frame
        student_frame =tkinter.LabelFrame(left_frame,bd=0,relief=RIDGE,font = ('calibri', 15,), text=" ",bg='white')
        student_frame.place(x=5,y=80,width=750,height=480)

        
        studentId_label =tkinter.Label(student_frame,text= "Student ID (Default Auto Increment)", bd=0,relief=RIDGE,font = ('calibri', 15,), bg='white', fg="black")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W, columnspan = 2)
        studentID_entry=ttk.Entry(student_frame, textvariable=self.var_id,state="disable", width=10,font = ('calibri', 15,))
        studentID_entry.grid(row=0, column=2,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame,text= "First Name",  bd=0,relief=RIDGE,font = ('calibri', 15,), bg='white', fg="black")
        studentId_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame, textvariable=self.var_fname, width=20,font = ('calibri', 15,))
        studentID_entry.grid(row=1, column=1,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Last Name",bg='white')
        studentId_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20, textvariable=self.var_lname, font = ('calibri', 15,))
        studentID_entry.grid(row=1, column=4,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Email",bg='white')
        studentId_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_email,font = ('calibri', 15,))
        studentID_entry.grid(row=2, column=1,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Phone",bg='white')
        studentId_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20, textvariable=self.var_phone,font = ('calibri', 15,))
        studentID_entry.grid(row=2, column=4,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Roll No.",bg='white')
        studentId_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_roll,font = ('calibri', 15,))
        studentID_entry.grid(row=3, column=1,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Enrollment No.",bg='white')
        studentId_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_enroll,font = ('calibri', 15,))
        studentID_entry.grid(row=3, column=4,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame, bd=0,relief=RIDGE,font = ('calibri', 15,), text="Division",bg='white')
        studentId_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,textvariable=self.var_div,width=20,font = ('calibri', 15,))
        studentID_entry.grid(row=4, column=1,padx=10, pady=10, sticky=W)

        studentId_label =tkinter.Label(student_frame,bd=0,relief=RIDGE,font = ('calibri', 15,), text="DOB",bg='white')
        studentId_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)
        studentID_entry=ttk.Entry(student_frame,textvariable=self.var_dob, width=20,font = ('calibri', 15,))
        studentID_entry.grid(row=4, column=4,padx=10, pady=10, sticky=W)

        btn_frame = tkinter.Frame(student_frame, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=724, height=45)
        
        
        save_btn=tkinter.Button(btn_frame, text="Save", command=self.add_data, width=23, font = ('calibri', 15,), relief=RIDGE, bg="white")
        save_btn.grid(row=0, column=0)

        
        update_btn=tkinter.Button(btn_frame, text="Update", command=self.update_data, width=23, font = ('calibri', 15,), relief=RIDGE, bg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=tkinter.Button(btn_frame, text="Delete",command=self.delete_data, width=23, font = ('calibri', 15,), relief=RIDGE, bg="white")
        delete_btn.grid(row=0, column=2)

        btn_frame1 = tkinter.Frame(student_frame, bd=0, relief=RIDGE)
        btn_frame1.place(x=0, y=305, width=724, height=45)

        reset_btn=tkinter.Button(btn_frame1, text="Reset", command=self.reset_data,  width=35, font = ('calibri', 15,), relief=RIDGE, bg="white")
        reset_btn.grid(row=0, column=3)

        takephoto_btn=tkinter.Button(btn_frame1, text="Take Photo", command=self.generate_dataset, width=35, font = ('calibri', 15,), relief=RIDGE, bg="white")
        takephoto_btn.grid(row=0, column=4)

        # Right Title Frame
        right_frame =tkinter.LabelFrame(main_frame,bd=0,relief=FLAT,font = ('calibri', 20,), text="Existing Students Module",bg='white')
        right_frame.place(x=768,y=10,width=768,height=750)

        # Right Table Frame 
        table_frame=tkinter.Frame(right_frame, bd=0, bg="white")
        table_frame.place(x=5, y=5, width=710, height=500)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

      

        self.student_table=ttk.Treeview(table_frame, column=("id", "dept", "sem", "fName", "lName", "email", "phone", "rno", "eno", "divi", "dob"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

# select dept, sem, fName, lName, email, phone, rollNo, enrollNo, divi, dob from user_table
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="ID")
        self.student_table.heading("dept",text="Dept")
        self.student_table.heading("sem",text="Sem")
        self.student_table.heading("fName",text="F. Name")
        self.student_table.heading("lName",text="L. Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("rno",text="Roll No.")
        self.student_table.heading("eno",text="Enroll. No.")
        self.student_table.heading("divi",text="Div")
        self.student_table.heading("dob",text="D.O.B")
        
        self.student_table["show"]="headings"

        self.student_table.column("id", width=50)
        self.student_table.column("dept", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("fName", width=100)
        self.student_table.column("lName", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("rno", width=100)
        self.student_table.column("eno", width=100)
        self.student_table.column("divi", width=100)
        self.student_table.column("dob", width=100)

        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_enroll.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "Please Verify All Fields", parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO user_table (fname,lname,email,phone,rollNo,enrollNo,dept,divi,sem,dob) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                    self.var_fname.get(),
                                                                                                                                                                    self.var_lname.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_enroll.get(),
                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                    self.var_dob.get()
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student can now access SpyCrop", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Couldn't Insert Data. Code:{str(es)}", parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
        my_cursor=conn.cursor()
        my_cursor.execute("select id, dept, sem, fName, lName, email, phone, rollNo, enrollNo, divi, dob from user_table")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_id.set(data[0]),
        self.var_dept.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_fname.set(data[3]),
        self.var_lname.set(data[4]),
        self.var_email.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_enroll.set(data[8]),
        self.var_div.set(data[9]),
        self.var_dob.set(data[10])

    
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_enroll.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "Please Verify All Fields", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the student record?", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE user_table SET dept=%s, sem=%s, fName=%s, lName=%s, email=%s, phone=%s, rollNo=%s, enrollNo=%s, divi=%s, dob=%s WHERE id=%s", (
                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                    self.var_fname.get(),
                                                                                                                                                                    self.var_lname.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_enroll.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_id.get()
                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Record Updates Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error", f"Something Went Wrong. Code:{str(es)}", parent=self.root)


    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error", "Student ID Number is Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student", "Are You Sure You Want to Remove this Student?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM user_table WHERE id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student Record Dropped Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Something Went Wrong. Code:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_sem.set("Select Semester")
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_roll.set("")
        self.var_enroll.set("")
        self.var_div.set("")
        self.var_dob.set("")
        self.var_id.set("")
        

        # OpenCV Dataset Generation

    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_enroll.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "Please Verify All Fields", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM user_table")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id=self.var_id.get()
                my_cursor.execute("UPDATE user_table SET dept=%s, sem=%s, fName=%s, lName=%s, email=%s, phone=%s, rollNo=%s, enrollNo=%s, divi=%s, dob=%s WHERE id=%s", (
                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                self.var_fname.get(),
                                                                                                                                                                self.var_lname.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_enroll.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_id.get()
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load OpenCV Frontal Face Pre-defined Data

                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(videosrc) # 3 - MI Camera / 0 - PC Camera  / 1 - DroidCam
                img_id=0
                while True:
                    try:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="studentdata/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50, 50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)
                    except Exception as e:
                        # For Showing Exceptions, Add the Following to Message Box Text - Error Code: \n {e} 
                        messagebox.showerror("Error", f"Make Sure You are Facing the Camera and your face is visible, then click OK to retry. Please do not interrupt while capturing the dataset. ",  parent=self.root)
                        break
                    if cv2.waitKey(1)==13 or int(img_id) == 200:
                        messagebox.showinfo("Success", f"Generating Dataset Successful. Please Train the AI now to ensure accuracy.")
                        break
                cap.release()
                cv2.destroyAllWindows()

                # messagebox.showinfo("Result","Generating AI Dataset Successful")

    def main(self):
        import studentmain
        self.new_window=(self.root)
        self.app=studentmain.Face_Recognition_System(self.new_window)

    
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()