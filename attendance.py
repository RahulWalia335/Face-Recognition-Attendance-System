from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student's Attendance")


    #Variables
        self.var_att=StringVar()
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_sec=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

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
        
        title_lbl=Label(self.root,text="...STUDENT'S ATTENDANCE SHEET...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=130,width=1530,height=45)
        
        main_frame=Frame( self.root, bd=2)
        main_frame.place(x=20,y=200,width=1485,height=670)

        #Left LabelFrame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Details",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Left_frame.place(x=10,y=10,width=600,height=580)



        #Current Course label
        Currentcourse_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        Currentcourse_frame.place(x=5,y=10,width=575,height=550)




        #Attendance ID
        id_label=Label(Currentcourse_frame,text="Attendance ID", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        id_label.grid(row=0,column=0,padx=15,sticky=W)
        id_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_att,font=("Bahnschrift Condensed",10,"bold"))
        id_text.grid(row=0,column=1,padx=1,pady=10,sticky=W)


        
        #University  RollNo.
        roll_label=Label(Currentcourse_frame,text="University RollNo", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        roll_label.grid(row=0,column=2,padx=15,sticky=W)
        roll_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_rollno,font=("Bahnschrift Condensed",10,"bold"))
        roll_text.grid(row=0,column=3,padx=1,pady=10,sticky=W)



        #Student's Name
        name_label=Label(Currentcourse_frame,text="Student's Name", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        name_label.grid(row=1,column=0,padx=15,sticky=W)
        name_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_name,font=("Bahnschrift Condensed",10,"bold"))
        name_text.grid(row=1,column=1,padx=1,pady=10,sticky=W)



        
        #Sec
        sec_label=Label(Currentcourse_frame,text="Sec", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        sec_label.grid(row=1,column=2,padx=15,sticky=W)
        sec_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_sec,font=("Bahnschrift Condensed",10,"bold"))
        sec_text.grid(row=1,column=3,padx=1,pady=10,sticky=W)



        
        #Time
        time_label=Label(Currentcourse_frame,text="Time", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        time_label.grid(row=2,column=0,padx=15,sticky=W)
        time_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_time,font=("Bahnschrift Condensed",10,"bold"))
        time_text.grid(row=2,column=1,padx=1,pady=10,sticky=W)



        
        #Date
        date_label=Label(Currentcourse_frame,text="Date", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        date_label.grid(row=2,column=2,padx=15,sticky=W)
        date_text=ttk.Entry(Currentcourse_frame,width=30,textvariable=self.var_date,font=("Bahnschrift Condensed",10,"bold"))
        date_text.grid(row=2,column=3,padx=1,pady=10,sticky=W)




        #Status
        status_label=Label(Currentcourse_frame,text="Status", font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        status_label.grid(row=3,column=0,padx=15,sticky=W)
        status_combo=ttk.Combobox(Currentcourse_frame,textvariable=self.var_status,font=("Bahnschrift Condensed",10,"bold"),width=26,state="readonly")
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=1,padx=1,pady=10,sticky=W)


        #Button Frame
        btn_frame=Frame(Currentcourse_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=570,height=165)

        import_btn=Button(btn_frame,text="Import.csv",command=self.importCsv,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        import_btn.grid(row=0,column=0,padx=10,pady=15)

        export_btn=Button(btn_frame,text="Export.csv",command=self.exportCsv,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        export_btn.grid(row=0,column=1,padx=10,pady=15)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=32)
        reset_btn.grid(row=0,column=2,padx=10,pady=15)



        #Right LabelFrame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Preview",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Right_frame.place(x=620,y=10,width=850,height=580)


        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="black")
        table_frame.place(x=5,y=20,width=825,height=470)
        
        #===========Scroll Bar Table===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","rollno","sec","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("rollno",text="RollNo")
        self.AttendanceReportTable.heading("sec",text="Sec")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("sec",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    #=======Fetch Data========
    def fetch_data(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
    
    #Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(file) as myfile:
             csvread=csv.reader(myfile,delimiter=",")
             for i in csvread:
                mydata.append(i)
        self.fetch_data(mydata)
    
    #Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found",parent=self.root)
                return False
            file=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(file,"w",newline="") as myfile:
                export=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export.writerow(i)
                    messagebox.showinfo("Success","Data Exported")
        except Exception as es:
                    messagebox.showerror("Error!!",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_att.set(rows[0])
        self.var_rollno.set(rows[1])
        self.var_name.set(rows[2])
        self.var_sec.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    #=============Reset===========
    def reset_data(self):
        self.var_att.set("")
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_sec.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")    



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()