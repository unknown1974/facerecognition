from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]
class attendence:
   def __init__(self, root):
      self.root=root
      self.root.geometry("1920x1100+0+0")
      self.root.title("face Recogniton System")


      #***variables**
      self.var_atten_id=StringVar()
      self.var_atten_roll=StringVar()
      self.var_atten_name=StringVar()
      self.var_atten_dep=StringVar()
      self.var_atten_time=StringVar()
      self.var_atten_date=StringVar()
      self.var_atten_attendence=StringVar()


      #first image
      img=Image.open(r"materials\atm1.png")
      img=img.resize((960,250))
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=960,height=250)

      #second image
      img2=Image.open(r"materials\atm2.jpg")
      img2=img2.resize((960,250))
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=960,y=0,width=960,height=250)

      #background image this is not mandatory its our own will
      img3=Image.open(r"materials\background1.jpg")
      img3=img3.resize((1920,830))
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=250,width=1920,height=830)

      title_lbl=Label(bg_img,text="ATTANDENCE     MANAGEMENT    SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
      title_lbl.place(x=0,y=0,width=1920,height=60)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=20,y=80,width=1880,height=730)


   #    #left label
      left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
      left_frame.place(x=10,y=10,width=920,height=700)

      img_left=Image.open(r"materials\atmtop.jpg")
      img_left=img_left.resize((920,130))
      self.photoimg_left=ImageTk.PhotoImage(img_left)
      
      f_lbl=Label(left_frame,image=self.photoimg_left)
      f_lbl.place(x=0,y=0,width=920,height=130)

      left_insideframe=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
      left_insideframe.place(x=10,y=140,width=895,height=520)

   #label and entry
   #    #attendence id
      attendenceId_label=Label(left_insideframe,text="AttendenceId : ",font=("consicansns",11,"bold"),bg="white")
      attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

      attendenceId_entry=ttk.Entry(left_insideframe,width=22,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
      attendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
      

      #Roll No
      rolllabel=Label(left_insideframe,text="Roll No : ",bg="white",font=("consicansns",11,"bold"))
      rolllabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

      atten_roll=ttk.Entry(left_insideframe,width=22,textvariable=self.var_atten_name,font=("consicansns",11,"bold"))
      atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

      #date
      namelabel=Label(left_insideframe,text="Name : ",bg="white",font=("consicansns",11,"bold"))
      namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

      atten_name=ttk.Entry(left_insideframe,textvariable=self.var_atten_name,width=22,font=("consicansns",11,"bold"))
      atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

      #department
      deplabel=Label(left_insideframe,text="Department",bg="white",font=("consicansns",11,"bold"))
      deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

      atten_dep=ttk.Entry(left_insideframe,textvariable=self.var_atten_dep,width=22,font=("consicansns",11,"bold"))
      atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

      #time
      timelabel=Label(left_insideframe,text="Time :",bg="white",font="consicansns 11 bold")
      timelabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

      atten_time=ttk.Entry(left_insideframe,textvariable=self.var_atten_time,width=22,font=("consicansns",11,"bold"))
      atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

      # Date
      datelabel=Label(left_insideframe,text="Date : ",bg="white",font="consicansns 11 bold")
      datelabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

      atten_time=ttk.Entry(left_insideframe,textvariable=self.var_atten_date,width=22,font=("consicansns",11,"bold"))
      atten_time.grid(row=2,column=3,padx=10,pady=5,sticky=W)

      #attendence
      attendencelabel=Label(left_insideframe,text="Attendance",bg="white",font="consicansns 11 bold")
      attendencelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

      self.atten_status=ttk.Combobox(left_insideframe,textvariable=self.var_atten_attendence,width=20,font="consicsans 11 bold",state="readonly")
      self.atten_status["values"]=("status","Present","Absent")
      self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)
      self.atten_status.current(0)

      #button frame
      btn_frame=Frame(left_insideframe,bd=2,bg="white",relief=RIDGE)
      btn_frame.place(x=0,y=350,width=890,height=60)

      save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=2)
      save_btn.grid(row=0,column=0,padx=5,pady = 5)

      update_btn=Button(btn_frame,text="Export Csv",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=2)
      update_btn.grid(row=0,column=1,padx=5,pady = 5)
      
      delete_btn=Button(btn_frame,text="Update",command=self.get_cursor,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=2)
      delete_btn.grid(row=0,column=2,padx=5,pady = 5)

      reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=2)
      reset_btn.grid(row=0,column=3,padx =2,pady = 5)



   #    #right label
      right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
      right_frame.place(x=950,y=10,width=910,height=700)
      
      table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
      table_frame.place(x=10,y=0,width=885,height=600)


      #**********scroll bar table**********
      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
      self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.AttendanceReportTable.xview)
      scroll_y.config(command=self.AttendanceReportTable.yview)

      self.AttendanceReportTable.heading("id",text="Attendance ID")
      self.AttendanceReportTable.heading("roll",text="Roll")
      self.AttendanceReportTable.heading("name",text="Name")
      self.AttendanceReportTable.heading("department",text="Department")
      self.AttendanceReportTable.heading("time",text="Time")
      self.AttendanceReportTable.heading("date",text="Date")
      self.AttendanceReportTable.heading("attendance",text="Attendence")


      self.AttendanceReportTable["show"]="headings"
      
      self.AttendanceReportTable.column("id",width=100)
      self.AttendanceReportTable.column("roll",width=100)
      self.AttendanceReportTable.column("name",width=100)
      self.AttendanceReportTable.column("department",width=100)
      self.AttendanceReportTable.column("time",width=100)
      self.AttendanceReportTable.column("date",width=100)
      self.AttendanceReportTable.column("attendance",width=100)

      self.AttendanceReportTable.pack(fill=BOTH,expand=1)

      self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
      


   #  #***************fecth data********************

   def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
         self.AttendanceReportTable.insert("",END,values=i)
      
    #import Csv
   def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("Al1 File","*.*")),parent=self.root)
      with open(fln) as myfile:
         csvread=csv.reader(myfile,delimiter=",")
         for i in csvread:
            mydata.append(i)
         self.fetchData(mydata)
       
     #export Csv
   def exportCsv(self):
      try:
         if len(mydata)<1:
            messagebox.showerror("No Data","No Data found to export",parent=self.root)
            return False
         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("Al1 File","*.*")),parent=self.root)
         with open(fln,mode="w",newline="") as myfile:
            exp_write=csv.writer(myfile,delimiter=",")
            for i in mydata:
               exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
      except Exception as es:
         messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    

   def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content["values"]
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendence.set(rows[6])
      
   def reset_data(self):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content["values"]
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendence.set("")

if __name__=="__main__":
   root=Tk()
   obj=attendence(root)
   root.mainloop()