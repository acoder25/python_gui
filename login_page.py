from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
from stu_mainpage import Libsystem
from main_pagesub import Libsystem1
 
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("login form")
        self.root.geometry("1550x800+0+0")
        
 
        def Myclick():
            def verify_login_details(user_type, username, password):
                conn = get_database_connection(user_type)
                c = conn.cursor()
 
                if user_type == "Student":
                    c.execute("SELECT * FROM stus WHERE name=? AND roll=?", (username, password))
                elif user_type == "Admin":
                    c.execute("SELECT * FROM admins WHERE name=? AND id=?", (username, password))
                else:
                    raise ValueError("Invalid user type")

                if user_type=="Student":
 
                    user_data = c.fetchone()
                    conn=sqlite3.connect("selected_student.db")
                    c=conn.cursor()
                    print(user_data)
     
                    c.execute('''DELETE FROM sel_students''')
                    c.execute('''INSERT INTO sel_students (name, roll, books,year, idate, Fine)
                     VALUES (?, ?, ?, ?, ?,?)''', (user_data[0], user_data[1], user_data[2], user_data[3], user_data[4],user_data[5]))
                    conn.commit()
     
                    conn.close()
     
                    return user_data

                elif user_type=="Admin":
                    user_data=c.fetchone()
                    return user_data

 
            # Function to get the database connection
            def get_database_connection(user_type):
                if user_type == "Student":
                    conn = sqlite3.connect('student.db')
                elif user_type == "Admin":
                    conn = sqlite3.connect('admin.db')
                else:
                    raise ValueError("Invalid user type")
                return conn
 
            user_type = user_type_var.get()
            username = e1.get()
            password = e2.get()
 
            try:
                user_data = verify_login_details(user_type, username, password)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
 
            if user_data:
                if user_type == "Student":
                    messagebox.showinfo("INFO","LOGIN successful!!!")
                    # If login successful as student, create and display the student info page
                    self.new_window=Toplevel(self.root)
                    self.app=Libsystem(self.new_window)
                    
 
                elif user_type == "Admin":
                    messagebox.showinfo("INFO","LOGIN successful!!!")
                    self.new_window=Toplevel(self.root)
                    self.app=Libsystem1(self.new_window)
                    
                    
 
            else:
                messagebox.showerror("Error", "Invalid username or password")
 
            # Function to verify login details
            
            
 
 
 
 
 
        root.configure(background="#E3FEF7")
 
        I4 = Image.open(r"C:\Users\User\Desktop\nitkkr1.jpg")
        new_img4 = I4.resize((1550, 800))
        my_img4 = ImageTk.PhotoImage(new_img4)
        I5 = Image.open(r"C:\Users\User\Desktop\nitkkr2.jpg")
        new_img5 = I5.resize((1550, 800))
        my_img5 = ImageTk.PhotoImage(new_img5)
 
        global our_images,count
        count=-1
        our_images=[my_img4,my_img5]
        #create a canvas//>>
        my_canvas=Canvas(root,width=1550,height=800)
        my_canvas.place(x=0,y=0)
 
        my_canvas.create_image(0,0,image=our_images[0],anchor='nw')
 
        def next():
            global count
            if count==1:
                my_canvas.create_image(0,0,image=our_images[0],anchor='nw')
                count=0
            else:
                my_canvas.create_image(0,0,image=our_images[count+1],anchor='nw')
                count+=1
            root.after(2000,next)
 
        next()
 
        #label for login page//>>
        lbl_login=Label(root,text="WELCOME TO NIT KURUSHETRA!",font=("comic sans ms",22,"bold"),bg="#77B0AA",relief=RAISED)
        lbl_login.place(x=0,y=0,width=1550,height=80)  
 
        my_frame101=LabelFrame(root,bd=2,relief=RIDGE,text="Enter Login Details:",font=("comic sans ms", 17, "bold"),bg="#BED7DC")
        my_frame101.place(x=490,y=480,width=550,height=210)          
 
        my_label2 = Label(my_frame101, text="USERNAME:", background="#BED7DC",font=("comic sans ms",14,"bold"))
        my_label2.place(x=20,y=20)
 
        e1 = Entry(my_frame101, width=50, borderwidth=3, relief="sunken")
        e1.place(x=150,y=25)
 
        my_label3 = Label(my_frame101, text="PASSWORD:  ", background="#BED7DC",font=("comic sans ms",14,"bold"))
        my_label3.place(x=20,y=70)
 
        e2 = Entry(my_frame101, width=50, borderwidth=3, relief="sunken")
        e2.place(x=150,y=75)
 
        my_button = Button(my_frame101, text="SUBMIT", padx=20, pady=5, command=Myclick, fg="black", background="#77B0AA",font=("comic sans ms",13,"bold"))
        my_button.place(x=350,y=110)
 
        user_type_var = StringVar(value="student")
        radio_student = Radiobutton(my_frame101, text="Student",fg="black", background="#BED7DC",font=("comic sans ms",13,"bold"),variable=user_type_var, value="Student")
        radio_student.place(x=150,y=115)
 
        radio_admin = Radiobutton(my_frame101, text="Admin",fg="black", background="#BED7DC",font=("comic sans ms",13,"bold"),variable=user_type_var, value="Admin")
        radio_admin.place(x=50,y=115)
 
        #footer label
 
        footer_label=Label(root,text="Copyright © 2024 National Institute of Technology Kurukshetra. All Rights Reserved.\n CONTACT US:110-2304-306",bd=4,relief="raised",bg="#77B0AA",font=("comic sans ms", 15, "bold"))
        footer_label.place(x=0,y=700,height=100,width=1550)
 
        self.root.mainloop()
 
if __name__=="__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()
