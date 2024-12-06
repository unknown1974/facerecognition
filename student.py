from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # ===============Variable===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()




        #first image
        
        img1 = Image.open(r"materials\Stu_top.jpeg")
        img1 = img1.resize((640,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=640,height=130)
        
        #second image

        img2 = Image.open(r"materials\Stu_mid.jpg")
        img2 = img2.resize((640,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=640,y=0,width=640,height=130)

        #third image

        img3 = Image.open(r"materials\Stu_top.jpeg")
        img3 = img3.resize((640,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1280,y=0,width=640,height=130)

        #background image

        img4 = Image.open(r"materials\Stu_background.jpg")
        img4 = img4.resize((1920,950))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1920,height=950)

        title_lbl = Label(bg_img,text="STUDENT    MANAGEMENT    SYSTEM",font=("times new roman",35,"bold"),bg="lightgrey",fg="green")
        title_lbl.place(x=0,y=0,width=1920,height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=70,width=1880,height=950)
       
        #left label

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=920,height=830)



        img_left=Image.open(r"materials\left_lebel.jpg")
        img_left=img_left.resize((920,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=1,y=0,width=915,height=130)
        
        #current course

        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=910,height=130)

        #Department

        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,pady=5,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width="20")
        dep_combo["values"]=("select department","IT","MCA","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # #course

        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width="20")
        course_combo["values"]=("select course","FE","BE","TE","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year

        Year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width="20")
        Year_combo["values"]=("select Year","2024-25","2023-24","2022-23","2021-22")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester

        Semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width="20")
        Semester_combo["values"]=("select Semester","sem-1","sem-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information

        Class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=270,width=910,height=530)

        #student ID

        StudentID_label=Label(Class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12))
        StudentID_entry.grid(row=0,column=1,pady=5,padx=10,sticky=W)

        #Student Name
        StudentName_label=Label(Class_Student_frame,text="StudentName:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,pady=5,padx=10,sticky=W)

        StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12))
        StudentName_entry.grid(row=0,column=3,pady=5,padx=10,sticky=W)

        #Student Division
        StudentDivision_label=Label(Class_Student_frame,text="StudentDivision:",font=("times new roman",12,"bold"),bg="white")
        StudentDivision_label.grid(row=1,column=0,pady=5,padx=10,sticky=W)

        
        StudentDivision_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width="18")
        StudentDivision_combo["values"]=("select","A","B","C","D","E")
        StudentDivision_combo.current(0)
        StudentDivision_combo.grid(row=1,column=1,pady=5,padx=10,sticky=W)

        #Student RollNo
        StudentRollNo_label=Label(Class_Student_frame,text="RollNo:",font=("times new roman",12,"bold"),bg="white")
        StudentRollNo_label.grid(row=1,column=2,pady=5,padx=10,sticky=W)

        StudentRollNo_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12))
        StudentRollNo_entry.grid(row=1,column=3,pady=5,padx=10,sticky=W)

        #Student Gender
        StudentGender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        StudentGender_label.grid(row=2,column=0,pady=5,padx=10,sticky=W)

        StudentGender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width="18")
        StudentGender_combo["values"]=("select","Male","Female","Other")
        StudentGender_combo.current(0)
        StudentGender_combo.grid(row=2,column=1,pady=5,padx=10,sticky=W)

        #Teacher Name
        TeacherName_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        TeacherName_label.grid(row=2,column=2,pady=5,padx=10,sticky=W)

        TeacherName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12))
        TeacherName_entry.grid(row=2,column=3,pady=5,padx=10,sticky=W)
        
        #Student Dob
        StudentDob_label=Label(Class_Student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        StudentDob_label.grid(row=3,column=0,pady=5,padx=10,sticky=W)

        StudentDob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        StudentDob_entry.grid(row=3,column=1,pady=5,padx=10,sticky=W)

        #Student Address
        StudentAddress_label=Label(Class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        StudentAddress_label.grid(row=3,column=2,pady=5,padx=10,sticky=W)

        TeacherName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12))
        TeacherName_entry.grid(row=3,column=3,pady=5,padx=10,sticky=W)

        #Student Email
        StudentEmail_label=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        StudentEmail_label.grid(row=4,column=0,pady=5,padx=10,sticky=W)

        StudentEmail_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        StudentEmail_entry.grid(row=4,column=1,pady=5,padx=10,sticky=W)

        #Student Phone No
        StudentMNo_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        StudentMNo_label.grid(row=4,column=2,pady=5,padx=10,sticky=W)

        StudentMNo_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        StudentMNo_entry.grid(row=4,column=3,pady=5,padx=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take a Photo Sample",value=YES)
        radiobutton1.grid(row=6,column=0)

        
        radiobutton2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value=NO)
        radiobutton2.grid(row=6,column=1)

        # Button Frame 
        btn_frame = Frame(Class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=1,y=230,width=903,height=60)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,pady=10,padx=10)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,pady=5,padx=5)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,pady=5,padx=5)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,pady=5,padx=5)

        btn_frame1 = Frame(Class_Student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=1,y=290,width=903,height=250)

        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=28,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,pady=10,padx=10)

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=28,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=0,pady=10,padx=10)

        # #right label

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12))
        right_frame.place(x=960,y=10,width=900,height=830)

        img_right=Image.open(r"materials\left_lebel.jpg")
        img_right=img_right.resize((910,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=1,y=0,width=900,height=130)


        # =============Search System==============

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=140,width=885,height=85)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="lightgreen")
        search_label.grid(row=0,column=0,pady=5,padx=10,sticky=W)

        Search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width="15")
        Search_combo["values"]=("Default","Roll No","Name","Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12))
        Search_entry.grid(row=0,column=2,pady=5,padx=10,sticky=W)

        search_btn = Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,pady=5,padx=5)

        showAll_btn = Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,pady=5,padx=5)

        # ===========table frame============

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=230,width=885,height=570)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("Dept","course","year","sem","id","name","div","roll","dob","gender","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("dob",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ================function declaration===============

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='3008',database='face_recogniser')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Detail has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent = self.root)


    # =============fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='3008',database='face_recogniser')
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student");
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ===========get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ==========update function============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update data",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='3008',database='face_recogniser')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Student details Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)
        

    # ===========delete function==========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is mandatory!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Conform to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='3008',database='face_recogniser')
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Details Deleted!",parent = self.root)

            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    # ==========Reset Data==========
    def reset_data(self):
        self.var_dep.set("select department")
        self.var_course.set("select course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select"),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("") 

    # ===========Generate data or Take a photo sample================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='3008',database='face_recogniser')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id =0
                for x in myresult:
                    id+=1;
                my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ===========load predefined data on face frontal from open cv===============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbour =5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="D:/Face Recognition System/data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break;
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)


        



if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()