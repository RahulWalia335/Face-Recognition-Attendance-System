from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Detection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognize")

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
        title_lbl=Label(self.root,text="...FACE DETECTOR...", font=("Bahnschrift Condensed",35,"bold"),bg="white", fg="purple")
        title_lbl.place(x=0,y=175,width=1530,height=45)

    #Recognize Button
        recognize_btn=Button(self.root,text="Face Recognize",command=self.face_recog,font=("Bahnschrift Condensed",10,"bold"),bg="skyblue", fg="purple",width=301)
        recognize_btn.place(x=5,y=300,height=45)

    #===========Attendance==============
    def attendance(self,i,n,r,s):
        with open("Rahul.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (s not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{s},{dt},{d1},Present")



    
    #=========Face Recognizer=======
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)   
            
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=pymysql.connect(host="localhost",user="root",password="",database="face")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select sec from student where id="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)

                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"rollno:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"sec:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attendance(i,n,r,s)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                
                coord=[x,y,w,h]     
            return coord

        def recognize(img,clf,faceCascade):
            cord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognizer",img)

            if cv2.waitKey(1)==13:
              break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Detection(root)
    root.mainloop()