from tkinter import*
from tkinter import filedialog
import sqlite3
import random
from PIL import ImageTk, Image
 
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT'S INFO")
        self.root.geometry("1291x440+258+253")
 
        #fetching student's information//>>
        title=Label(self.root,text="YOUR DETAILS:",font=("comic sans ms", 15, "bold"),bg="#77B0AA",fg="white")
        title.place(x=0,y=0,width=1291,height=50)
 
        label_frame_mid=LabelFrame(self.root,bd=2,relief=RIDGE,text="HELLO USER!",font=("comic sans ms", 19, "bold"))
        label_frame_mid.place(x=100,y=50,width=1100,height=335)
 
        # connection with the database
        conn= sqlite3.connect("selected_student.db")
        c=conn.cursor()
 
        c.execute("SELECT name FROM sel_students")
        rows=c.fetchone()
        row=rows[0]
        print(rows)
 
        #labels for student's details//>>
        stu_name=Label(label_frame_mid,text="NAME:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_name.grid(row=0,column=0,pady=15,padx=10)
        e_stu_name=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row))
        e_stu_name.grid(row=0,column=1,pady=15,padx=10)
 
        c.execute("SELECT roll FROM sel_students")
        rows1=c.fetchone()
        row1=rows1[0]
        print(rows1)
 
        stu_roll=Label(label_frame_mid,text="ROLL NO:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_roll.grid(row=1,column=0,pady=15,padx=10)
        e_stu_roll=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row1))
        e_stu_roll.grid(row=1,column=1,pady=15,padx=10)
 
 
        c.execute("SELECT idate FROM sel_students")
        rows2=c.fetchone()
        row2=rows2[0]
        print(rows2)
 
        stu_issue=Label(label_frame_mid,text="ISSUED DATE:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_issue.grid(row=2,column=0,pady=15,padx=10)
        e_stu_issue=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row2))
        e_stu_issue.grid(row=2,column=1,pady=15,padx=10)
 
        c.execute("SELECT books FROM sel_students")
        rows3=c.fetchone()
        row3=rows3[0]
        print(rows3)
 
        stu_issuedate=Label(label_frame_mid,text="ISSUED BOOK:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_issuedate.grid(row=0,column=3,pady=15,padx=20)
        e_stu_issuedate=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row3))
        e_stu_issuedate.grid(row=0,column=4,pady=15,padx=10)
 
        c.execute("SELECT fine FROM sel_students")
        rows4=c.fetchone()
        row4=rows4[0]
        print(rows4)
 
        stu_fine=Label(label_frame_mid,text="FINE:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_fine.grid(row=1,column=3,pady=15,padx=20)
        e_stu_fine=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row4))
        e_stu_fine.grid(row=1,column=4,pady=15,padx=10)
 
        c.execute("SELECT year FROM sel_students")
        rows5=c.fetchone()
        row5=rows5[0]
        print(rows5)
 
        stu_year=Label(label_frame_mid,text="YEAR:",font=("comic sans ms", 17, "bold"),pady=10)
        stu_year.grid(row=2,column=3,pady=15,padx=20)
        e_stu_year=Label(label_frame_mid,width=22,font=("comic sans ms", 15, "bold"),text="{}".format(row5))
        e_stu_year.grid(row=2,column=4,pady=15,padx=10)
 
        conn.commit()
        conn.close()
 
 
        # def upload_photo():
        #     global photo_img  # Making photo_img global
        #     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")])
        #     if filepath:
        #         photo = Image.open(filepath)
        #         photo.thumbnail((200, 200))  # Resize the image
        #         photo_img = ImageTk.PhotoImage(photo)
 
        # photo_img_label = Label(label_frame_mid)
        # photo_img_label.place(x=800, y=50)
 
        # #button to upload photo//>>
        # upload_btn=Button(label_frame_mid,text="Upload Photo",font=("comic sans ms", 12, "bold"),command=upload_photo)
        # upload_btn.place(x=800,y=200)
 
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()