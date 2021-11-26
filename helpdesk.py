from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")


        title_lbl=Label(self.root,text="...Contact Me...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=30,width=1530,height=45)
        
        main_frame=Frame(self.root, bd=2)
        main_frame.place(x=20,y=200,width=1485,height=670)

        l1_label=Label(main_frame,text="Email ID : rwalia335@gmail.com", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l1_label.place(x=0,y=40)

        l2_label=Label(main_frame,text="Linked Profile: https://www.linkedin.com/in/rahul-walia-627158217/", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l2_label.place(x=0,y=100)

        l3_label=Label(main_frame,text="Github Link:  https://github.com/RahulWalia335", font=("Bahnschrift Condensed",20,"bold"),bg="white", fg="black")
        l3_label.place(x=0,y=160)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()