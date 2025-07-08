from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import mysql.connector
import cv2
from datetime import datetime
from mysql.connector.locales.eng import client_error

videosrc = 1  # 3 - MI Camera / 0 - PC Camera  / 1 - DroidCam

class Face_Recognition:
    def __init__(self,root):
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Train SpyCrop AI")
        self.root.configure(bg='#101820')
        root.state('zoomed')
        

        img=Image.open(r"img\facerec.jpg")
        img=img.resize((width, height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-2,y=0,width=2160,height=820)

        b1 = tkinter.Button(root, text = 'Start Attendance Manager', command=self.face_recog , activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=RIDGE, font=("calibri", 25))
        b1.place(x=335,y=382,height=100,width=400)

        exitbtn = tkinter.Button(root, text = 'Back',command=self.main, activebackground='#101820', activeforeground="white",bd=0, bg='#101820', fg="white", relief=FLAT, font=("calibri", 25))
        exitbtn.place(x=335,y=580,height=100,width=400)

    def mark_attendance(self, i, r, n, d):
            now = datetime.now()
            date = now.strftime("%d-%m-%y")
            
            with open(f"staffattendance/{date}.csv", "a+", newline="") as f:
                mydatalist = f.readlines()
                name_list = []
                for line in mydatalist:
                    entry = line.split((","))
                    name_list.append(entry[0])
                    i = str(i)
                if ((n not in name_list) and (d not in name_list) and (r not in name_list) and (
                        i not in name_list)):
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%y")
                    dtstring = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{n},{d},{r},{d1},{dtstring},present")




    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf ):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="spycrop")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT fname, lname FROM host_table WHERE personId="+str(id))
                n = my_cursor.fetchone()
                n =" ".join(n)

                my_cursor.execute("SELECT staffid FROM host_table WHERE personId="+str(id))
                r = my_cursor.fetchone()
                r ="+".join(r)

                my_cursor.execute("SELECT dept FROM host_table WHERE personId="+str(id))
                d = my_cursor.fetchone()
                d ="+".join(d)

                
                

 

                if confidence>83:
                    cv2.putText(img,f"ID: {id}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),1)
                    cv2.putText(img,f"Name: {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),1)
                    cv2.putText(img,f"Department: {d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),1)
                    cv2.putText(img,f"Staff ID: {r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),1)
                    self.mark_attendance(id,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,f"Unidentified Individual",(x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),1) 

                coord=[x,y,w,y]

            return coord
        
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("staffclassifier.xml")

        video_cap=cv2.VideoCapture(videosrc, cv2.CAP_DSHOW) # 3 - MI Camera / 2 PC Camera
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            img.astype('uint8')
            cv2.imshow("SpyCrop extends a Warm Welcome to you.", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def main(self):
        import staffmain
        self.new_window=(self.root)
        self.app=staffmain.Face_Recognition_System(self.new_window)
      

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()      
