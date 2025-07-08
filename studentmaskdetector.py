import os
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import mysql.connector
import cv2
from datetime import datetime
import csv
import time
import schedule
import smtplib
import ssl
import schedule
import threading
from mysql.connector.locales.eng import client_error
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

videosrc = 0  #/ 0 - PC Camera  / 1 - MI Camera


class Mask_Recognition:
    def __init__(self, root):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root = root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Train SpyCrop AI")
        self.root.configure(bg='#101820')
        root.state('zoomed')

        img = Image.open(r"img\maskalert.jpg")
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-2, y=0, width=2160, height=820)

        b1 = tkinter.Button(root, text='Start Mask Detector', command=self.face_recog, activeforeground="#ffffff",
                            activebackground='#101820', bd=0, bg='#101820', fg="#ffffff", relief=RIDGE, font=("calibri", 25))
        b1.place(x=335,y=382,height=100,width=400)

        exitbtn = tkinter.Button(root, text='Back', command=self.main, activebackground='#101820',
                                 activeforeground="white", bd=0, bg='#101820', fg="white", relief=FLAT, font=("calibri", 25))
        exitbtn.place(x=335,y=580,height=100,width=400)

    def mark_attendance(self, i, r, n, e, d):
        now = datetime.now()
        date = now.strftime("%d-%m-%y")
        d1 = now.strftime("%d/%m/%y")
        dtstring = now.strftime("%H:%M:%S")

        with open(f"studentalerts/{date}.csv", "w+", newline="\n") as f:
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
                    f.writelines(f"{i},{n},{e},{d},{r},{d1},{dtstring},No Mask\n")
        
        with open(f"studentalertmails/{date}.csv", "w+", newline="\n") as f:
                mydatalist = f.readlines()
                name_list = []
                for line in mydatalist:
                    entry = line.split((","))   
                    name_list.append(entry[0])
                if (e not in name_list):
                    f.writelines(f"\n{e}")

                        

    def face_recog(self):
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("studentclassifier.xml")

        cap = cv2.VideoCapture(videosrc) # Video source capturing
        cap.set(3, 640) # Width of the video window
        cap.set(4, 480) # Height of the video window
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Face detector
        maskClassifier = load_model('maskclassifier.model') # Mask classifier

        while True:

            _, frame = cap.read() # Reading frame from video source

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Converting RGB to Grayscale
            
            faces = faceCascade.detectMultiScale( # Detecting faces
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                )
            
            for (x, y, h, w) in faces: 

                faceROI = frame[y : y + h, x : x + w, :] # Cropping face region of interest

                faceROI = cv2.resize(faceROI, (160, 160)) # Resizing faceROI to 160x160
                                                        # Because, Our VGG16 model accepts 160x160 as input 
                faceROI = img_to_array(faceROI)
                faceROI = faceROI.reshape(1, 160, 160, 3) # Changing dimensions to 1x160x160x3, Because our VGG16 
                                                        # take input as 4D matrix(BATCH_SIZE, 160, 160, #Channels)

                prediction = maskClassifier(faceROI) # Making predictions
                (withoutmask, withmask) = prediction[0].numpy()
                
                id, predict = clf.predict(gray[y:y+h, x:x+w])
                confidence = int((10*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="", database="spycrop")
                my_cursor = conn.cursor()
                
                # id = 27

                my_cursor.execute(
                    "SELECT fname, lname FROM `user_table` WHERE id="+str(id))
                n = my_cursor.fetchone()
                n = " ".join(n)

                my_cursor.execute(
                    "SELECT rollNo FROM `user_table` WHERE id="+str(id))


                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "SELECT dept FROM `user_table` WHERE id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "SELECT email FROM `user_table` WHERE id="+str(id))
                e = my_cursor.fetchone()
                e = "+".join(e)
                
                # Drawing bounding boxes using OpenCV
                if withmask > withoutmask:
                    (label, color, prob) = ('Mask', (0, 255, 0), withmask*100)
                else:
                    (label, color, prob) = ('No mask', (0, 0, 255), withoutmask*100)
                    self.mark_attendance(id, r, n, e, d)


            # (label, color, prob) = ('Mask', (0, 255, 0), withmask*100.0) if withmask > withoutmask else ('No mask', (0, 0, 255), withoutmask*100.0)

                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                cv2.rectangle(frame, (x + 15, y + 2), (x + w - 15, y + 20), (0, 0, 0), -1) #lower
                cv2.rectangle(frame, (x + 15, y - 2), (x + w - 15, y - 20), (0, 0, 0), -1) #upper

                cv2.putText(frame, str(prob)+' %', (x + 20, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.putText(frame, label, (x + 20, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

                
            cv2.imshow('Video', frame) # Displaying the video
            

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        cap.release() # Releasing the capture
        cv2.destroyAllWindows()



    def main(self):
        import studentmain
        self.new_window = (self.root)
        self.app = studentmain.Face_Recognition_System(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Mask_Recognition(root)
    root.mainloop()
    



