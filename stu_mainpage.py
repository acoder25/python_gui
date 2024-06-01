from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel
from student_info import student
from online_library import my_library
from tkinter import ttk
from functools import partial
import webbrowser
from audiobooks import my_audios
from about_sub import About_us
from notification import my_notification
 
 
 
class Libsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT'S PAGE")
        self.root.geometry("1550x800+0+0")
# logo
        I1 = Image.open(r"C:\Users\User\Desktop\logo.png")
        new_img1 = I1.resize((150, 120))
        my_img1 = ImageTk.PhotoImage(new_img1)
        l2 = Label(root, image=my_img1)
        l2.place(x=0, y=0)
# side image
        I2 = Image.open(r"C:\Users\User\Desktop\lib.jpg")
        new_img2 = I2.resize((1400, 120))
        my_img2 = ImageTk.PhotoImage(new_img2)
        I3 = Image.open(r"C:\Users\User\Desktop\background.jpg")
        new_img3 = I3.resize((1400, 120))
        my_img3 = ImageTk.PhotoImage(new_img3)
 
        global our_images,count
        count=-1
        our_images=[my_img2,my_img3]
        #create a canvas//>>
        my_canvas=Canvas(root,width=1400,height=120)
        my_canvas.place(x=150,y=0)
 
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
# ----------------------------------------------------------------------------------------------------------------------------------------
        def logout():
            # Close the current window
            root.destroy()
            # Open the login page window or frame
            open_login_page()
 
        def open_login_page():
            root = Tk()
            root.title("login form")
            root.geometry("1550x800+0+0")
            root.iconbitmap(r"C:\Users\asus\OneDrive\Pictures\login_image.png")
 
            def Myclick():
                user_type = user_type_var.get()
                username=e1.get()
                password=e2.get()
 
                conn1=sqlite3.connect('student_database.db' if user_type == "Student" else 'admin_database.db')
                c=conn1.cursor()
 
                # verify login details
 
                if user_type == "student":
                    c.execute("SELECT * FROM students WHERE name=? AND rollno=?", (username, password))
                else:
                    c.execute("SELECT * FROM admins WHERE name=? AND adminId=?", (username, password))
    
                user_data = c.fetchone()
 
 
                if user_data:
                    if user_type == "student":
                        # If login successful as student, fetch student details
                        name, rollno, Issue_date, Fine, CurrentDate = user_data
                        # Display student info
                        info_label.config(text=f"Name: {name}\nRoll No: {rollno}\nIssue Date: {Issue_date}\nFine: {Fine}\nCurrent Date: {CurrentDate}")
                    else:
                        # If login successful as admin, fetch admin details
                        adminID, name, _ = user_data
                        # Display admin info
                        info_label.config(text=f"Admin ID: {adminID}\nUsername: {name}\nAdmin Type: {user_type}")
                else:
                    messagebox.showerror("Error", "Invalid username or password")
 
                conn1.close()
 
            root.configure(background="#E3FEF7")
 
            I4 = Image.open(r"C:\Users\asus\OneDrive\Pictures\nitkkr.jpg")
            new_img4 = I4.resize((1550, 800))
            my_img4 = ImageTk.PhotoImage(new_img4)
            I5 = Image.open(r"C:\Users\asus\OneDrive\Pictures\nitkkr2.jpg")
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
 
            user_type_var = tk.StringVar(value="student")
            radio_student = Radiobutton(my_frame101, text="Student",fg="black", background="#BED7DC",font=("comic sans ms",13,"bold"),variable=user_type_var, value="Student")
            radio_student.place(x=150,y=115)
 
            radio_admin = tk.Radiobutton(my_frame101, text="Admin",fg="black", background="#BED7DC",font=("comic sans ms",13,"bold"),variable=user_type_var, value="Admin")
            radio_admin.place(x=50,y=115)
 
            #footer label
 
            footer_label=Label(root,text="Copyright © 2024 National Institute of Technology Kurukshetra. All Rights Reserved.\n CONTACT US:110-2304-306",bd=4,relief="raised",bg="#77B0AA",font=("comic sans ms", 15, "bold"))
            footer_label.place(x=0,y=700,height=100,width=1550)
 
            root.mainloop()
 
# title
        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("comic sans ms",18,"bold"),bg="#007F73",relief=SUNKEN)
        lbl_title.place(x=0,y=120,width=1550,height=50)
 
        logout_button=Button(root, text="LOGOUT", command=logout,bg="white",fg="black",font=("times new roman",10,"bold"))
        logout_button.place(x=1350,y=130,height=30,width=100)
 
        # status bar
 
        #drop down menu in my account//>>
        def show_dropdown_menu(event):
            dropdown_menu.tk_popup(event.x_root, event.y_root)
 
        my_button = Button(root, text="MY ACCOUNT", fg="white", background="#382b58",
                           font=("comic sans ms", 15, "bold"), relief="raised")
        my_button.place(x=0, y=170, width=310, height=50)
        my_button.bind("<Button-1>", show_dropdown_menu)
 
        # Dropdown menu for My Account
        options = ["Student Info"]
        dropdown_menu = Menu(root, tearoff=0, fg="white", bg="#382b58", font=("comic sans ms", 15, "bold"))
        for option in options:
            dropdown_menu.add_command(label=option, command=lambda opt=option:self.open_window(opt))
         #--------------------------------------------------------------------------------------------------------------------------------
        def library():
            self.new_window=Toplevel(self.root)
            self.app=my_library(self.new_window)
 
        def audio():
            self.new_window=Toplevel(self.root)
            self.app=my_audios(self.new_window)
 
        def about():
            self.new_window=Toplevel(self.root)
            self.app=About_us(self.new_window)
 
        def notification():
            self.new_window=Toplevel(self.root)
            self.app=my_notification(self.new_window)
 
 
        my_button1 = Button(root, text="ONLINE LIBRARY", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),relief="raised",command=library)
        my_button1.place(x=310, y=170, width=310, height=50)
 
        my_button2 = Button(root, text="AUDIOBOOKS", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),relief="raised",command=audio)
        my_button2.place(x=620, y=170, width=310, height=50)
        my_button3 = Button(root, text="NOTIFICATIONS", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                           relief="raised",command=notification)
        my_button3.place(x=930, y=170, width=310, height=50)
 
        my_button4 = Button(root, text="ABOUT US", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                            relief="raised",command=about)
        my_button4.place(x=1240, y=170, width=310, height=50)
 
        # side frame
        side_frame=Frame(root,bd=4,relief="raised",bg="#382b58")
        side_frame.place(x=0,y=220,height=480,width=258.33)
        my_button5=Button(side_frame,text="SWITCH ACCOUNT",fg="white",bg="#382b58",font=("comic sans ms", 15, "bold"),
                    relief="raised",command=logout)
        my_button5.place(x=0,y=425,height=50,width=258.33)
 
        #Quotes for side frame//>>
        global our_quotes,count1,text_id
        count1=-1
        our_quotes=["The more that you read,\n the more things you will \nknow. The more that\n you learn, the more \nplaces you'll go. \n- Dr. Seuss","Education is the most\n powerful weapon which\n you can use to\n change the world.\n - Nelson Mandela"]
        #create a canvas//>>
        my_canvas1=Canvas(root,width=258.33,height=430,background="#382b58",)
        my_canvas1.place(x=0,y=220)
 
        text_id=my_canvas1.create_text(0, 60, text=our_quotes[0], anchor='nw', font=("comic sans ms", 15, "bold"),fill="white")
 
        def next1():
            global count1, text_id
            # Increment count
            count1 = (count1 + 1) % len(our_quotes)
            # Update the text of the existing text item
            my_canvas1.itemconfig(text_id, text=our_quotes[count1])
            # Schedule the next update
            root.after(3000, next1)
 
        next1()
 
        #footer label
 
        footer_label=Label(root,text="Copyright © 2024 National Institute of Technology Kurukshetra. All Rights Reserved.\n CONTACT US:110-2304-306",bd=4,relief="raised",bg="#007F73",font=("comic sans ms", 15, "bold"))
        footer_label.place(x=0,y=695,height=100,width=1550)
 
        #clickable book icons
        my_frame=LabelFrame(root,bd=2,relief=RIDGE,text="POPULAR BOOKS",font=("comic sans ms", 19, "bold"))
        my_frame.place(x=260,y=220,width=1275,height=445)
 
        def open_book(event,link):
            webbrowser.open(link)
 
        # Load a book icon image//BOOK1 
        book_image1 = Image.open(r"C:\Users\User\Desktop\book1.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image1 = book_image1.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image1 = ImageTk.PhotoImage(book_image1)
 
        # Create a label with the book icon image
        book_label1 = Label(root, image=book_image1)
        book_label1.image=book_image1
        book_label1.place(x=290,y=330)
 
        # Bind the click event to the book label
        book_label1.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396742/read"))
 
        # Load a book icon image//BOOK2
        book_image2 = Image.open(r"C:\Users\User\Desktop\book2.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image2 = book_image2.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image2 = ImageTk.PhotoImage(book_image2)
 
        # Create a label with the book icon image
        book_label2 = Label(root, image=book_image2)
        book_label2.image=book_image2
        book_label2.place(x=600,y=330)
 
        # Bind the click event to the book label
        book_label2.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396744/read"))
 
        # Load a book icon image//BOOK3
        book_image3 = Image.open(r"C:\Users\User\Desktop\book3.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image3 = book_image3.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image3 = ImageTk.PhotoImage(book_image3)
 
        # Create a label with the book icon image
        book_label3 = Label(root, image=book_image3)
        book_label3.image=book_image3
        book_label3.place(x=910,y=330)
 
        # Bind the click event to the book label
        book_label3.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/127836/read"))
 
        # Load a book icon image//BOOK4
        book_image4 = Image.open(r"C:\Users\User\Desktop\book4.jpg")
        
        # Resize the image
        desired_width = 200  # Set your desired width
        desired_height = 250  # Set your desired height
        book_image4 = book_image4.resize((desired_width, desired_height))
 
        # Convert the resized image to a PhotoImage
        book_image4 = ImageTk.PhotoImage(book_image4)
 
        # Create a label with the book icon image
        book_label4 = Label(root, image=book_image4)
        book_label4.image=book_image4
        book_label4.place(x=1220,y=330)
 
        # Bind the click event to the book label
        book_label4.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396746/read"))
 
        self.root.mainloop()
        #student info//>>
    def open_window(self,option):
        if option=="Student Info":
            self.student_info()
 
    def student_info(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
 
 
if __name__=="__main__":
    root=Tk()
    obj = Libsystem(root)
    root.mainloop()
