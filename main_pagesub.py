from tkinter import *
from PIL import ImageTk, Image
from python_sub import Stu_corner
from tkinter import Toplevel
from about_sub import About_us
import webbrowser
from functools import partial
from catalog_sub import Catalog
from profile_sub import Profile_sub
from setting_sub import Setting
from threading import Thread

class Libsystem1:
    
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN PAGE")
        self.root.geometry("1550x800+0+0")
# logo
        I1 = Image.open(r"C:\Users\User\Desktop\logo.png")
        new_img1 = I1.resize((150, 120))
        my_img1 = ImageTk.PhotoImage(new_img1)
        l2 = Label(root, image=my_img1)
        l2.place(x=0, y=0)
# side image
        I = Image.open(r"C:\Users\User\Desktop\background.jpg")
        new_img = I.resize((1400, 120))
        my_img = ImageTk.PhotoImage(new_img)
        l1 = Label(root, image=my_img)
        l1.place(x=150, y=0)

        def enlarge_image(event):
            I4 = Image.open(r"C:\Users\User\Desktop\book1_cover.jpg")
            new_img4 = I4.resize((300, 300))
            my_img4 = ImageTk.PhotoImage(new_img4)
            l101 = Label(root, image=my_img4)
            l101.place(x=300, y=250)

        def restore_image(event):
            I3 = Image.open(r"C:\Users\User\Desktop\book1_cover.jpg")
            new_img3 = I3.resize((200, 200))
            my_img3 = ImageTk.PhotoImage(new_img3)
            l100 = Label(root, image=my_img3)
            l100.place(x=300, y=250)
           

        def open_webpage(event):
            webbrowser.open("https://example.com")

        def stu_details():
            self.new_window=Toplevel(self.root)
            self.app=Stu_corner(self.new_window)

        def about():
            self.new_window=Toplevel(self.root)
            self.app=About_us(self.new_window)

        def catalog():
            self.new_window=Toplevel(self.root)
            self.app=Catalog(self.new_window)

        def profile():
            self.new_window=Toplevel(self.root)
            self.app=Profile_sub(self.new_window)

        def settings_call():
            self.new_window=Toplevel(self.root)
            self.app=Setting(self.new_window)


        def logout():
            # Close the current window
            root.destroy()
            # Open the login page window or frame
            open_login_page()

        def open_login_page():
            root=root
            root.title("login form")
            root.geometry("1550x800+0+0")
            
     
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
     
            root.mainloop()
 

# title
        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("comic sans ms",18,"bold"),bg="#007F73")
        lbl_title.place(x=0,y=120,width=1550,height=50)

        logout_button=Button(root, text="LOGOUT", command=logout,bg="white",fg="black",font=("times new roman",10,"bold"))
        logout_button.place(x=1350,y=130,height=30,width=100)

        # status bar
        my_button = Button(root, text="STUDENT'S CORNER", fg="white", background="#382b58",font=("comic sans ms",15,"bold"),relief="raised",command=stu_details)
        my_button.place(x=0,y=170,width=310,height=50)


        my_button2 = Button(root, text="ABOUT US", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),command=about,
                           relief="raised")
        my_button2.place(x=310, y=170, width=310, height=50)
        my_button3 = Button(root, text="MANAGE CATALOG", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                           relief="raised",command=catalog)
        my_button3.place(x=620, y=170, width=310, height=50)

        my_button4 = Button(root, text="PROFILE", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                            relief="raised",command=profile)
        my_button4.place(x=930, y=170, width=310, height=50)
        my_button3 = Button(root, text="SETTINGS", fg="white", background="#382b58", font=("comic sans ms", 15, "bold"),
                            relief="raised",command=settings_call)
        my_button3.place(x=1240, y=170, width=310, height=50)
        # side frame
        side_frame=Frame(root,bd=4,relief="raised",bg="#382b58")
        side_frame.place(x=0,y=220,height=580,width=258.33)

        

        global our_quotes,count1,text_id
        count1=-1
        our_quotes=["The more that you\nread, the more things\nyou will know.The\nmore that you learn,\nthe more places\nyou'll go. -\nDr. Seuss","Education is the most \npowerful weapon which\nyou can use to change\nthe world.\n- Nelson Mandela"]
        #create a canvas//>>
        my_canvas1=Canvas(root,width=258.33,height=580,background="#382b58",)
        my_canvas1.place(x=0,y=220)
 
        text_id=my_canvas1.create_text(20, 50, text=our_quotes[0], anchor='nw', font=("comic sans ms",16, "bold"),fill="white")
 
        def next1():
            global count1, text_id
            # Increment count
            count1 = (count1 + 1) % len(our_quotes)
            # Update the text of the existing text item
            my_canvas1.itemconfig(text_id, text=our_quotes[count1])
            # Schedule the next update
            root.after(3000, next1)
 
        next1()

        b2=Button(my_canvas1,text="SWITCH ACCOUNT",background="#007F73",fg="black",font=("comic sans ms", 15, "bold"),relief="raised",bd=2,command=logout)
        b2.place(x=2,y=433,width=258.33,height=50)

 
 
        
        my_frame=LabelFrame(root,bd=2,relief=RIDGE,text="POPULAR BOOKS",font=("comic sans ms", 19, "bold"))
        my_frame.place(x=280,y=250,width=1220,height=600)

        footer_label=Label(root,text="Copyright © 2024 National Institute of Technology Kurukshetra. All Rights Reserved.\n CONTACT US:110-2304-306",bd=4,relief="raised",bg="#007F73",font=("comic sans ms", 15, "bold"))
        footer_label.place(x=0,y=700,height=100,width=1528)

        # main_frame = Frame(root, relief="raised")
        # main_frame.place(x=300, y=275, height=590, width=1250)       


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
        book_label1 = Label(my_frame, image=book_image1,padx=20)
        book_label1.image=book_image1
        book_label1.place(x=100,y=100)
 
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
        book_label2 = Label(my_frame, image=book_image2,padx=20)
        book_label2.image=book_image2
        book_label2.place(x=400,y=100)
 
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
        book_label3 = Label(my_frame, image=book_image3,padx=20)
        book_label3.image=book_image3
        book_label3.place(x=700,y=100)
 
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
        book_label4 = Label(my_frame, image=book_image4)
        book_label4.image=book_image4
        book_label4.place(x=1000,y=100)
 
        # Bind the click event to the book label
        book_label4.bind("<Button-1>", partial(open_book, link="https://manybooks.net/book/396746/read"))
 

        self.root.mainloop()

if __name__=="__main__":
    root=Tk()
    obj = Libsystem1(root)
    root.mainloop()

