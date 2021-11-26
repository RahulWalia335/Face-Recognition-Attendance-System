from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer's Info")


        title_lbl=Label(self.root,text="...DEVELOPER...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=30,width=1530,height=45)
        
        main_frame=Frame(self.root, bd=2)
        main_frame.place(x=20,y=200,width=1485,height=670)

        #Developer Button
        img7=Image.open(r"C:\Users\rahul\Desktop\Face-Recognition-Attendance System\developer.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        #Developer(Image)
        f1=Label(self.root,image=self.photoimg7,cursor="hand2")
        f1.place(x=40,y=200,width=370,height=420)


        #Right LabelFrame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="About Me",font=("Bahnschrift Condensed",10,"bold"),bg="white", fg="purple")
        Right_frame.place(x=420,y=0,width=850,height=480)
        
        l1_label=Label(Right_frame,text="Hi guys my name is Rahul Walia, currently pursuing B.Tech in Computer Science from Graphic", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l1_label.place(x=0,y=40)

        l2_label=Label(Right_frame,text="Era Hill University. I'm currently in 3rd year (5th sem).I have worked on Face Recognition", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l2_label.place(x=0,y=100)

        l3_label=Label(Right_frame,text="Attendance System using Python, tkinter", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l3_label.place(x=0,y=160)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()