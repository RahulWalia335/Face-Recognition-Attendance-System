from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Model Training")

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
        title_lbl=Label(self.root,text="...MODEL TRAINING...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=175,width=1530,height=45)


        #Train Button
        train_btn=Button(self.root,text="Train Data Model",command=self.train_classifier,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=301)
        train_btn.place(x=5,y=300,height=45)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
            

        for image in path:
            img=Image.open(image).convert('L')   #grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=======Train Classifier========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()