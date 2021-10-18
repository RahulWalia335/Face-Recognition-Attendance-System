from tkinter import*
from tkinter import ttk
import tkinter
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk
import os
from student import Student
from training import Train
from face_recognize import Face_Detection
from attendance import Attendance
from developer import Developer
from helpdesk import Help


class Face_Recognition_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_Attendance_System")

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
        

        title_lbl=Label(bg_img,text="...FACE RECOGNITION ATTENDANCE SYSTEM...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         

        #Student Button
        img4=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\student.jfif")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        #Student_Details(Image)
        b1=Button(bg_img,image=self.photoimg4,command=self.details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        #Student_Details(Text)
        b1_1=Button(bg_img,text="STUDENT'S INFORMATION",command=self.details,cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)



        #Face Detection Button
        img5=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\face.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        #Face Detection(Image)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        #Face Detection(Text)
        b1_1=Button(bg_img,text="FACE DETECTION",cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)



        #Attendance Button
        img6=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\attendance.jfif")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        #Attendance(Image)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)

        #Attendance(Text)
        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red",command=self.attendance)
        b1_1.place(x=800,y=300,width=220,height=40)



        #Developer Button
        img7=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\developer.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        #Developer(Image)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.developer)
        b1.place(x=1100,y=100,width=220,height=220)

        #Developer(Text)
        b1_1=Button(bg_img,text="DEVELOPER INFO",cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red",command=self.developer)
        b1_1.place(x=1100,y=300,width=220,height=40)



        #Photos
        img8=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\photos.jfif")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        #Photos(Image)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=200,y=400,width=220,height=220)

        #Photos(Text)
        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red",command=self.open_img)
        b1_1.place(x=200,y=600,width=220,height=40)



        #Model Training
        img9=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\model.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        #Model Training(Image)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=500,y=400,width=220,height=220)

        #Model Training(Text)
        b1_1=Button(bg_img,text="MODEL TRAINING",cursor="hand2",command=self.train_data,font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=500,y=600,width=220,height=40)



        #Help Desk
        img10=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\help.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        #Help Desk(Image)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.help)
        b1.place(x=800,y=400,width=220,height=220)

        #Help Desk(Text)
        b1_1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help,font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=800,y=600,width=220,height=40)



        #Exit
        img11=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\exit.jfif")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        #Exit(Image)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=400,width=220,height=220)

        #Exit(Text)
        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.exit,font=("Bahnschrift Condensed",15,"bold"),bg="white", fg="red")
        b1_1.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    #==============Function Buttons=============
    def details(self):
     self.details=Toplevel(self.root)
     self.app=Student(self.details)

    def train_data(self):
     self.details=Toplevel(self.root)
     self.app=Train(self.details)

    def face_data(self):
     self.details=Toplevel(self.root)
     self.app=Face_Detection(self.details)


    def attendance(self):
      self.details=Toplevel(self.root)
      self.app=Attendance(self.details)

    def developer(self):
      self.details=Toplevel(self.root)
      self.app=Developer(self.details)

    def help(self):
      self.details=Toplevel(self.root)
      self.app=Help(self.details)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("!!!","Are you Sure to exit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Attendance_System(root)
    root.mainloop()
