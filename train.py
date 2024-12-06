from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
import cv2
import os
import numpy as np
import face_recognition 

     
class train:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recogniton System")
        title_lbl=Label(self.root,text="Train        Data          Set", font=("times new roman",35,"bold"),bg="lightgreen",fg="red")
        title_lbl.place(x=0,y=0,width=1920,height=50)

        # ========top images=========

        img_top1=Image.open(r"materials\train_topl.png")
        img_top1=img_top1.resize((640,325))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=50,width=640,height=325)

        img_top2=Image.open(r"materials\train_topc.jpg")
        img_top2=img_top2.resize((640,325))
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=640,y=50,width=640,height=325)

        img_top3=Image.open(r"materials\train_topr.png")
        img_top3=img_top3.resize((640,325))
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(self.root,image=self.photoimg_top3)
        f_lbl.place(x=1280,y=50,width=640,height=325)


        # =========button==========

        b1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1.place(x=0,y=375,width=1920,height=60)
        
        img_bottom=Image.open(r"materials\train_btm1.jpeg")
        img_bottom=img_bottom.resize((1920,645))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=435,width=1920,height=645)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  #grey scale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])  

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids =np.array(ids)

        # ===========Train the classifier============
        clf=cv2.face.LBPHFaceRecognizer.create()
        # clf = face_recognition.Face()

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainig dataset completed!",parent=self.root)


        



if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()