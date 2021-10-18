from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student's Informtion")


        #==========Variables==========
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_rollno=StringVar()
        self.var_fathername=StringVar()
        self.var_sec=StringVar()
        self.var_course=StringVar()
        self.var_branch=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_teachername=StringVar()
    

        #image1
        img=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\image1.jpg")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        #image2
        img1=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\image4.jfif")
        img1=img1.resize((510,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=515,y=0,width=510,height=130)


        #image3
        img2=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\image1.jpg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1030,y=0,width=510,height=130)

        #background_Image
        img3=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\image5.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        

        title_lbl=Label(bg_img,text="...STUDENT'S INFORMATION...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame( bg_img, bd=2)
        main_frame.place(x=20,y=55,width=1485,height=710)

        #Left LabelFrame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Details",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Left_frame.place(x=10,y=10,width=600,height=580)

        #Current Course label
        Currentcourse_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        Currentcourse_frame.place(x=5,y=10,width=575,height=550)



        #Student's Name
        name_label=Label(Currentcourse_frame,text="Student's Name", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        name_label.grid(row=0,column=0,padx=15,sticky=W)
        name_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_name,font=("Bahnschrift Condensed",10,"bold"))
        name_text.grid(row=0,column=1,padx=1,pady=10,sticky=W)



        #Student's ID
        id_label=Label(Currentcourse_frame,text="Student's ID", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        id_label.grid(row=0,column=2,padx=15,sticky=W)
        id_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_id,font=("Bahnschrift Condensed",10,"bold"))
        id_text.grid(row=0,column=3,padx=1,pady=10,sticky=W)



        #University  RollNo.
        roll_label=Label(Currentcourse_frame,text="University RollNo", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        roll_label.grid(row=1,column=0,padx=15,sticky=W)
        roll_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_rollno,font=("Bahnschrift Condensed",10,"bold"))
        roll_text.grid(row=1,column=1,padx=1,pady=10,sticky=W)



        #Father's Nmae
        father_label=Label(Currentcourse_frame,text="Father's Name", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        father_label.grid(row=1,column=2,padx=15,sticky=W)
        father_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_fathername,font=("Bahnschrift Condensed",10,"bold"))
        father_text.grid(row=1,column=3,padx=1,pady=10,sticky=W)



        #Sec
        sec_label=Label(Currentcourse_frame,text="Sec", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        sec_label.grid(row=2,column=0,padx=15,sticky=W)
        sec_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_sec,font=("Bahnschrift Condensed",10,"bold"))
        sec_text.grid(row=2,column=1,padx=1,pady=10,sticky=W)



        #Course
        course_label=Label(Currentcourse_frame,text="Course", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        course_label.grid(row=2,column=2,padx=15,sticky=W)
        course_combo=ttk.Combobox(Currentcourse_frame,textvariable=self.var_course,font=("Bahnschrift Condensed",10,"bold"),width=26,state="readonly")
        course_combo["values"]=("Select Course","B.tech","B.Sc","B.Com","BCA","MBA")
        course_combo.current(0)
        course_combo.grid(row=2,column=3,padx=1,pady=10,sticky=W)



        #Branch
        branch_label=Label(Currentcourse_frame,text="Branch", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        branch_label.grid(row=3,column=0,padx=15,sticky=W)
        branch_combo=ttk.Combobox(Currentcourse_frame,textvariable=self.var_branch,font=("Bahnschrift Condensed",10,"bold"),width=26, state="readonly")
        branch_combo["values"]=("Select Branch","Computer Science","Mechanical Engineering","Civil Engineering","IT","Specialization")
        branch_combo.current(0)
        branch_combo.grid(row=3,column=1,padx=1,pady=10,sticky=W)



        #Year
        year_label=Label(Currentcourse_frame,text="Year", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        year_label.grid(row=3,column=2,padx=15,sticky=W)
        year_combo=ttk.Combobox(Currentcourse_frame,textvariable=self.var_year,font=("Bahnschrift Condensed",10,"bold"),width=26,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=3,column=3,padx=1,pady=10,sticky=W)



        #Semester
        sem_label=Label(Currentcourse_frame,text="Semester", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        sem_label.grid(row=4,column=0,padx=15,sticky=W)
        search_combo=ttk.Combobox(Currentcourse_frame,textvariable=self.var_sem,font=("Bahnschrift Condensed",10,"bold"),width=26, state="readonly")
        search_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        search_combo.current(0)
        search_combo.grid(row=4,column=1,padx=1,pady=10,sticky=W)



        #Student's Email
        email_label=Label(Currentcourse_frame,text="Email", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        email_label.grid(row=4,column=2,padx=15,sticky=W)
        email_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_email,font=("Bahnschrift Condensed",10,"bold"))
        email_text.grid(row=4,column=3,padx=1,pady=10,sticky=W)



        #Student's Phone
        phone_label=Label(Currentcourse_frame,text="Phone No", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        phone_label.grid(row=5,column=0,padx=15,sticky=W)
        phone_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_phoneno,font=("Bahnschrift Condensed",10,"bold"))
        phone_text.grid(row=5,column=1,padx=1,pady=10,sticky=W)



        #Student's Address
        address_label=Label(Currentcourse_frame,text="Address", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        address_label.grid(row=5,column=2,padx=15,sticky=W)
        search_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_address,font=("Bahnschrift Condensed",10,"bold"))
        search_text.grid(row=5,column=3,padx=1,pady=10,sticky=W)



        #Student's Date Of Birth
        dob_label=Label(Currentcourse_frame,text="DOB", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        dob_label.grid(row=6,column=0,padx=15,sticky=W)
        dob_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_dob,font=("Bahnschrift Condensed",10,"bold"))
        dob_text.grid(row=6,column=1,padx=1,pady=10,sticky=W)



        #Teacher's Name
        phone_label=Label(Currentcourse_frame,text="Teacher's Name", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        phone_label.grid(row=6,column=2,padx=15,sticky=W)
        phone_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_teachername,font=("Bahnschrift Condensed",10,"bold"))
        phone_text.grid(row=6,column=3,padx=1,pady=10,sticky=W)



        #Radio Buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(Currentcourse_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        
        radio2=ttk.Radiobutton(Currentcourse_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio2.grid(row=7,column=1,padx=10,pady=10,sticky=W)



        #Button Frame
        btn_frame=Frame(Currentcourse_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=350,width=570,height=165)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        save_btn.grid(row=0,column=0,padx=10,pady=15)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        update_btn.grid(row=0,column=1,padx=10,pady=15)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        delete_btn.grid(row=0,column=2,padx=10,pady=15)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        reset_btn.grid(row=1,column=0,padx=10,pady=15)

        upload_btn=Button(btn_frame,text="Upload Sample",command=self.generate_dataset,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        upload_btn.grid(row=1,column=1,padx=10,pady=15)



        
        #Right LabelFrame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Preview",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Right_frame.place(x=620,y=10,width=850,height=580)



        #===================Table===================
        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        table_frame.place(x=5,y=40,width=825,height=470)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("name","id","rollno","father","sec","course","branch","year","sem","email","phone","address","dob","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name",text="Student's Name")
        self.student_table.heading("id",text="Student's ID")
        self.student_table.heading("rollno",text="University RollNo")
        self.student_table.heading("father",text="Father's Name")
        self.student_table.heading("sec",text="Sec")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("branch",text="Branch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("teacher",text="Teacher's Name")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("name",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("father",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("branch",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("email",width=160)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        #============Function Declaration(ADD Data)==========
    def add_data(self):
        if self.var_name.get()=="" or self.var_id.get()=="" or self.var_rollno.get()=="" or self.var_fathername.get()=="" or self.var_sec.get()=="" or self.var_course.get()=="Select Course" or self.var_branch.get()=="Select Branch" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_email.get()=="" or self.var_phoneno.get()=="" or self.var_address.get()=="" or self.var_teachername.get()=="" or self.var_dob.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error!!","All fields are required",parent=self.root)
        else:
                try:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_id.get(),
                                                                                                                    self.var_rollno.get(),
                                                                                                                    self.var_fathername.get(),
                                                                                                                    self.var_sec.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_branch.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phoneno.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_teachername.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                 ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error!!",f"Due To:{str(es)}",parent=self.root)


    #=================FetchData=============
    def fetch_data(self):
     conn=pymysql.connect(host="localhost",user="root",password="",database="face")
     my_cursor=conn.cursor()
     my_cursor.execute("select * from student")
     data=my_cursor.fetchall()
     if len(data)!=0:
         self.student_table.delete(*self.student_table.get_children())
         for i in data:
             self.student_table.insert("",END,values=i)
             conn.commit()
     conn.close()

     #================GetCursor===============
    def get_cursor(self,event=""):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]
         self.var_name.set(data[0]),
         self.var_id.set(data[1]),
         self.var_rollno.set(data[2]),
         self.var_fathername.set(data[3]),
         self.var_sec.set(data[4]),
         self.var_course.set(data[5]),
         self.var_branch.set(data[6]),
         self.var_year.set(data[7]),
         self.var_sem.set(data[8]),
         self.var_email.set(data[9]),
         self.var_phoneno.set(data[10]),
         self.var_address.set(data[11]),
         self.var_dob.set(data[12]),
         self.var_teachername.set(data[13]),
         self.var_radio1.set(data[14])


    #====================Update Function=============
    def update_data(self):
        if self.var_name.get()=="" or self.var_id.get()=="" or self.var_rollno.get()=="" or self.var_fathername.get()=="" or self.var_sec.get()=="" or self.var_course.get()=="Select Course" or self.var_branch.get()=="Select Branch" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_email.get()=="" or self.var_phoneno.get()=="" or self.var_address.get()=="" or self.var_teachername.get()=="" or self.var_dob.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error!!","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update Student's Information",parent=self.root)
                if Update>0:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set name=%s,rollno=%s,father=%s,sec=%s,course=%s,branch=%s,year=%s,sem=%s,email=%s,phone=%s,address=%s,dob=%s,teacher=%s,photo=%s where id=%s",(
                                                                                                                                                               self.var_name.get(),                                                                                                                              
                                                                                                                                                               self.var_rollno.get(),
                                                                                                                                                               self.var_fathername.get(),
                                                                                                                                                               self.var_sec.get(),
                                                                                                                                                               self.var_course.get(),
                                                                                                                                                               self.var_branch.get(),
                                                                                                                                                               self.var_year.get(),
                                                                                                                                                               self.var_sem.get(),
                                                                                                                                                               self.var_email.get(),
                                                                                                                                                               self.var_phoneno.get(),
                                                                                                                                                               self.var_address.get(),
                                                                                                                                                               self.var_dob.get(),
                                                                                                                                                               self.var_teachername.get(),
                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                               self.var_id.get()
                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success!!","Details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


     #=============Delete Function================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error!","Student ID is required",parent=self.root)  
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete data",parent=self.root) 
                if delete>0:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()    
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #=============Reset===========
    def reset_data(self):
        self.var_name.set("")
        self.var_id.set("")
        self.var_rollno.set("")
        self.var_fathername.set("")
        self.var_sec.set("")
        self.var_course.set("Select Course")
        self.var_branch.set("Select Branch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_teachername.set("")
        self.var_rollno.set("")


    #===============Generate Dataset/Take Photos==============
    def generate_dataset(self):
        if self.var_name.get()=="" or self.var_id.get()=="" or self.var_rollno.get()=="" or self.var_fathername.get()=="" or self.var_sec.get()=="" or self.var_course.get()=="Select Course" or self.var_branch.get()=="Select Branch" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_email.get()=="" or self.var_phoneno.get()=="" or self.var_address.get()=="" or self.var_teachername.get()=="" or self.var_dob.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error!!","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                  id+=1
                my_cursor.execute("update student set name=%s,rollno=%s,father=%s,sec=%s,course=%s,branch=%s,year=%s,sem=%s,email=%s,phone=%s,address=%s,dob=%s,teacher=%s,photo=%s where id=%s",(
                                                                                                                                                               self.var_name.get(),                                                                                                                              
                                                                                                                                                               self.var_rollno.get(),
                                                                                                                                                               self.var_fathername.get(),
                                                                                                                                                               self.var_sec.get(),
                                                                                                                                                               self.var_course.get(),
                                                                                                                                                               self.var_branch.get(),
                                                                                                                                                               self.var_year.get(),
                                                                                                                                                               self.var_sem.get(),
                                                                                                                                                               self.var_email.get(),
                                                                                                                                                               self.var_phoneno.get(),
                                                                                                                                                               self.var_address.get(),
                                                                                                                                                               self.var_dob.get(),
                                                                                                                                                               self.var_teachername.get(),
                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                               self.var_id.get()==id+1
                                                                                                                                                         ))                                                                                                                                            
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=====Load Predefined Data On Face Frontals from Open CV=====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crop(myframe) is not None:
                           img_id+=1
                           face=cv2.resize(face_crop(myframe),(450,450))
                           face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                           file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                           cv2.imwrite(file_name,face)
                           cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                           cv2.imshow("Cropped Image",face)

                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset Completed!!",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root) 

                


     




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()