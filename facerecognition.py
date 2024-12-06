from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy
 
class facerecognition:
   def __init__(self,root):
      self.root=root
      self.root.geometry("1920x1080+0+0")
      self.root.title("face Recogniton System")
    
      title_lbl=Label(self.root,text="Face    Recognition", font=("times new roman",35,"bold"),bg="lightgreen",fg="red")
      title_lbl.place(x=0,y=0,width=1920,height=75)
     

      # =========bg image======
      img_bg=Image.open(r"materials\fc4.jpg")
      img_bg=img_bg.resize((1920,1005))
      self.photoimg_bg=ImageTk.PhotoImage(img_bg)

      f_lbl=Label(self.root,image=self.photoimg_bg)
      f_lbl.place(x=0,y=75,width=1920,height=1005)

      img_fg=Image.open(r"materials\fc3.png")
      img_fg=img_fg.resize((400,400))
      self.photoimg_fg=ImageTk.PhotoImage(img_fg)

      # =====fg button==========
      b1 = Button(f_lbl,image=self.photoimg_fg,cursor="hand2",command=self.face_recog)
      b1.place(x=760,y=250,width=400,height=400)

      b1_1 = Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="blue",fg="white")
      b1_1.place(x=760,y=650,width=400,height=80)

   # ===============attendance============
   def mark_attandance(self,i,r,n,d):
      with open("attandance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
               entry = line.split((","))
               name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
               now=datetime.now()
               d1=now.strftime("%d/%m/%Y")
               dtString=now.strftime("%H:%M:%S")
               f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


   #  ==========face recognition==========

   def face_recog(self):
      def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
         gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
         features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


         coord=[]


         for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)
            id, predict=clf.predict(gray_image[y:y+h,x:x+w])
            confidence=int((100*(1-predict/300)))

            conn=mysql.connector.connect(host="localhost", username="root", password="3008",database="face_recogniser")
            my_cursor=conn.cursor()

            # my_cursor.execute("select Name from face_recogniser.student where Student_id="+str(id))
            # n=my_cursor.fetchone()
            # n="+".join(n)

            # my_cursor.execute("select Dept from face_recogniser.student where Student_id="+str(id))
            # d= my_cursor.fetchone()
            # d="+".join(d)
            # my_cursor.execute("select Roll from face_recogniser.student where Student_id="+str(id))
            # r= my_cursor.fetchone()
            # r="+".join(r)

            my_cursor.execute("select Name from face_recogniser.student where Student_id="+str(id))
            n=my_cursor.fetchone()
            
            if n:
               n=str(n[0])  # Convert the tuple to a string
            else:
               n="Unknown"

            my_cursor.execute("select Dept from face_recogniser.student where Student_id = "+str(id))
            d= my_cursor.fetchone()
            if d:
               d=str(d[0])  # Convert the tuple to a string
            else:
               d="Unknown"
              

            my_cursor.execute("select roll from face_recogniser.student where Student_id="+str(id))
            r= my_cursor.fetchone()
            if r:
               r=str(r[0])  # Convert the tuple to a string
            else:
               r="Unknown"

            my_cursor.execute("select Student_id from face_recogniser.student where Student_id="+str(id))
            i= my_cursor.fetchone()
            if i:
               i=str(r[0])  # Convert the tuple to a string
            else:
               i="Unknown"


              
            if confidence>83:
               cv2.putText(img, f"ID:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
               cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
               cv2.putText(img, f"Name: {n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
               cv2.putText(img, f"Department: {d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255,255),3)
               self.mark_attandance(i,r,n,d)

            else:
               cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255),3)
               cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)


            coord=[x,y,w,y]
              
         return coord
      
      def recognize (img,clf, faceCascade):
         coord=draw_boundary(img,faceCascade, 1.1, 10, (255,25,255), "Face", clf)
         return img

      faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      clf=cv2.face.LBPHFaceRecognizer.create()
      clf.read("classifier.xml")

      video_cap=cv2.VideoCapture(0)
      
      while True:
         ret, img=video_cap.read()
         img=recognize(img,clf,faceCascade)
         cv2.imshow("Welcome to face recognition",img)
         if cv2.waitKey(1)==13:
            break
      video_cap.release()
      cv2.destroyAllWindows() 

                 

             
if __name__=="__main__":
    root=Tk()
    obj=facerecognition(root)
    root.mainloop()