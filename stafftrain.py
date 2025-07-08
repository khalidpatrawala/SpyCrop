
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        width= root.winfo_screenwidth() 
        height= root.winfo_screenheight()
        self.root=root
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Train SpyCrop AI")
        self.root.configure(bg='#101820')
        root.state('zoomed')
        

        img=Image.open(r"img\train.jpg")
        img=img.resize((width, height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-2,y=0,width=2160,height=820)

        b1 = tkinter.Button(root, command=self. train_clasifier, text = 'Begin to train SpyCrop AI.', activeforeground="#ffffff",activebackground='#101820',bd=0, bg='#101820', fg="#ffffff", relief=RIDGE, font=("calibri", 25))
        b1.place(x=490,y=382,height=100,width=400)

        exitbtn = tkinter.Button(root, text = 'Back',command=self.main, activebackground='#101820', activeforeground="white",bd=0, bg='#101820', fg="white", relief=FLAT, font=("calibri", 25))
        exitbtn.place(x=490,y=580,height=100,width=400)


    def train_clasifier(self):
        data_dir=("staffdata")
        path= [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')    # Gray Scale Image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("SpyCrop Computer Vision Trainer", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Classifier Training

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("staffclassifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Sucess","Training CV Datasets Completed.")

    def main(self):
        import staffmain
        self.new_window=(self.root)
        self.app=staffmain.Face_Recognition_System(self.new_window)





      
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()      