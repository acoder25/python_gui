from tkinter import*
from tkinter import filedialog
import random
from PIL import ImageTk, Image
import sqlite3
import os
 
class my_library():
    def __init__(self,root):
        self.root=root
        self.root.title("ONLINE LIBRARY")
        self.root.geometry("1550x800+0+0")
 
# logo
        I3 = Image.open(r"C:\Users\User\Desktop\logo.png")
        new_img3 = I3.resize((150, 120))
        my_img3 = ImageTk.PhotoImage(new_img3)
        l3 = Label(root, image=my_img3)
        l3.image=my_img3
        l3.place(x=0, y=0)
 
        lbl_title=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=("comic sans ms", 20, "bold"),bg="#77B0AA",relief=RAISED)
        lbl_title.place(x=150,y=0,width=1400,height=120)
 
# side frame
        def logout():
            # Close the current window
            root.destroy()
            # Open the login page window or frame
            open_login_page()
 
        def open_login_page():
            root = Tk()
            root.title("login form")
            root.geometry("1550x800+0+0")
            root.iconbitmap(r"C:\Users\User\Desktop\lib_icon.png")
 
        side_frame=Frame(root,bd=4,relief="raised",bg="#382b58")
        side_frame.place(x=0,y=120,height=680,width=258.33)
        my_button5=Button(side_frame,text="SWITCH ACCOUNT",fg="white",bg="#382b58",font=("comic sans ms", 15, "bold"),
                    relief="raised",command=logout)
        my_button5.place(x=0,y=620,height=50,width=258.33)
 
        lbl_title=Label(root,text="ONLINE LIBRARY",font=("comic sans ms",18,"bold"),bg="#382b58",fg="white")
        lbl_title.place(x=0,y=120,width=1550,height=50)
 
        #mid frame for books//>
 
        label_frame_mid=LabelFrame(self.root,bd=2,relief=RIDGE,text="READ ME!",font=("comic sans ms", 19, "bold"))
        label_frame_mid.place(x=258.33,y=170,width=1400,height=630)
 
 
 
        # Connect to the SQLite database
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
 
        # Fetch book data from the database
        cursor.execute("SELECT name, pdf_path, image_path FROM books")
        books = cursor.fetchall()
 
        # Close the database connection
        conn.close()
 
        # Function to open PDF file
        def open_pdf(pdf_path):
            try:
                os.startfile(pdf_path)
            except OSError:
                # Handle error if PDF file cannot be opened
                tk.messagebox.showerror("Error", "Unable to open PDF file.")
 
        # Loop through the books and display them
        books1=books[0:2]
        for book in range(len(books1)):
            name, pdf_path, image_path = books1[book]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img1 = I1.resize((200, 250))
            my_img1 = ImageTk.PhotoImage(new_img1)
            cover_label = Label(label_frame_mid, image=my_img1)
            cover_label.image=my_img1
            cover_label.grid(row=book,column=0,pady=20,padx=80)
 
    
            # Create a button to open the PDF file
            pdf_button = Button(label_frame_mid, text="OPEN", command=lambda path=pdf_path: open_pdf(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            pdf_button.grid(row=book,column=1)
 
        books2=books[2:4]
        for book in range(len(books2)):
            name, pdf_path, image_path = books2[book]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img1 = I1.resize((200, 250))
            my_img1 = ImageTk.PhotoImage(new_img1)
            cover_label = Label(label_frame_mid, image=my_img1)
            cover_label.image=my_img1
            cover_label.grid(row=book,column=2,pady=20,padx=60)
 
    
            # Create a button to open the PDF file
            pdf_button = Button(label_frame_mid, text="OPEN", command=lambda path=pdf_path: open_pdf(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            pdf_button.grid(row=book,column=3)
 
        books3=books[4:6]
        for book in range(len(books3)):
            name, pdf_path, image_path = books3[book]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img1 = I1.resize((200, 250))
            my_img1 = ImageTk.PhotoImage(new_img1)
            cover_label = Label(label_frame_mid, image=my_img1)
            cover_label.image=my_img1
            cover_label.grid(row=book,column=4,pady=20,padx=60)
 
    
            # Create a button to open the PDF file
            pdf_button = Button(label_frame_mid, text="OPEN", command=lambda path=pdf_path: open_pdf(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            pdf_button.grid(row=book,column=5)
 
 
if __name__=="__main__":
    root=Tk()
    obj=my_library(root)
    root.mainloop()
