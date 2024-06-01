from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox
from tkinter import Scrollbar 
 
 
 
class About_us:
 
    def __init__(self, root):
 
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")
        
       
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
 
            def Myclick():
                l3 = Label(root, text="form sumbitted !!", background="#FFFDD0")
                l3.grid(row=17, column=11)
 
            root.configure(background="#FFFDD0")
 
            l0 = Label(root, text="NIT\nKURUKSHETRA", font=("comic sans ms", 18, "bold"), background="#FFFDD0")
            l0.grid(row=0, column=4)
 
            I = Image.open(r"C:\Users\User\Desktop\lib_icon.png")
            new_img = I.resize((600, 400))
            my_img = ImageTk.PhotoImage(new_img)
            l1 = Label(root, image=my_img)
            l1.grid(row=0, column=13, columnspan=3)
 
            dummy_label_2 = Label(root, background="#FFFDD0")
            dummy_label_2.grid(row=1, column=0, padx=10, pady=10)
 
            dummy_enter = Label(root, background="#FFFDD0")
            dummy_enter.grid(row=3, column=2, padx=10, pady=10)
 
            dummy_entry1 = Label(root, background="#FFFDD0")
            dummy_entry1.grid(row=5, column=5, padx=10, pady=10)
 
            dummy_entry1 = Label(root, background="#FFFDD0")
            dummy_entry1.grid(row=7, column=7, padx=10, pady=10)
 
            my_label = Label(root, text="Enter details to login:  ", background="#FFFDD0",
                             font=('Helvetica', 18, 'bold'))
            my_label.grid(row=2, column=13)
 
            button_quit = Button(root, text="EXIT", command=root.quit, width=10)
            button_quit.grid(row=2, column=16)
 
            my_label2 = Label(root, text="ROLL NO:  ", background="#FFFDD0")
            my_label2.grid(row=4, column=14)
 
            e = Entry(root, width=30, borderwidth=3, relief="raised")
            e.grid(row=4, column=15)
 
            my_label3 = Label(root, text="PASSWORD:  ", background="#FFFDD0")
            my_label3.grid(row=6, column=14)
 
            e = Entry(root, width=30, borderwidth=3, relief="raised")
            e.grid(row=6, column=15)
 
            # dummy_entry2 = Label(root,background="#FFFDD0")
            # dummy_entry2.grid(row=13, column=10, padx=10, pady=10)
 
            my_button = Button(root, text="sumbit", padx=20, pady=5, command=Myclick, fg="white", background="black")
            my_button.grid(row=8,column=14)
 
            root.mainloop()
 
# title
 
        I2 = Image.open(r"C:\Users\User\Desktop\logo.png")
        new_img2 = I2.resize((120, 120))
        my_img2 = ImageTk.PhotoImage(new_img2)
        lb101 = Label(root, image=my_img2)
        lb101.image = my_img2  # Keep a reference to the image object
        lb101.place(x=0, y=0)
 
        lbl_title = Label(root, text="LIBRARY MANAGMENT SYSTEM", font=("comic sans ms", 20, "bold"), fg="white", bg="#77B0AA")
        lbl_title.place(x=120, y=0, width=1550, height=120)
 
        lb1 = Label(root, text="ABOUT US", font=("comic sans ms", 20, "bold"), fg="white", bg="#382b58")
        lb1.place(x=0, y=120, width=1550, height=80)
 
        b_home=Button(lb1,text="HOME", font=("comic sans ms", 20, "bold"), fg="white", bg="#382b58")
        b_home.place(x=0,y=0,height=80,width=140)
 
        side_frame=Frame(root,bd=4,relief="raised",bg="#77B0AA")
        side_frame.place(x=0,y=200,height=600,width=250)
 
        b2=Button(side_frame,text="SWITCH ACCOUNT",background="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised",bd=2,command=logout)
        b2.place(x=0,y=540,width=258.33,height=50)
        
       
        self.main_frame_text = Frame(root, bd=2, relief="raised")
        self.main_frame_text.place(x=260,y=220,height=550,width=645)
 
        self.main_frame_image = Frame(root, bd=2, relief="raised")
        self.main_frame_image.place(x=850,y=220,height=550,width=635)
 
 
       
        text_widget = Text(self.main_frame_text)
        text_widget.place(x=0,y=0,width=645,height=550)
        
 
        scroll_bar=Scrollbar(self.main_frame_text,orient="vertical")
        scroll_bar.pack(side="right",fill="y")
        
        
        content="""The library, initially set up in 1965, has grown in size, collection,\nand services.\nPresently, NIT Kurukshetra has a very  spacious library with a \ngood collection of documents, which includes text and\nreference books, CD-ROMs, and a large number of print\n and online journals and e-books.\n\nWith its growing resources, space, and services, the library\ncaters to the needs of faculty, researchers, scholars,\nand students.The library is a growing organism.
        \n To meet all the requirements, sufficient space has been added\n for stacking, reading, and other services.\nThe Library has a reading capacity of 500 readers and\n sufficient space for stacking new documents,\n a digital library and Audio audio-visual centre.\n The total area of the library at\n present is 36711sq-ft.\n
        ->Book Bank Facilities:\nThe Library Book Bank is one of the richest Book Banks\n in the country. All B. Tech, M.Tech, MBA and MCA\n students are given 6-8 books for the full\n semester from Book Bank.\n
        ->Library Hours:\nAll Working Days: 08.30 am to 05:30 pm\nSaturdays & Holidays: 09.00 am to 05.00 pm\n
        ->Reading Facilities: 24x07x365\n
        
        """
        italic_tag = text_widget.tag_configure("italic", font=("comic sans ms", 14, "italic"),background="#FFFFFF")
 
# Insert the content with the italic tag applied
        text_widget.insert(END, content, "italic")
 
        text_widget.config(state=DISABLED)
 
# setting images/>
        
        self.image_paths = [r"C:\Users\User\Desktop\nitkkr1.jpg", r"C:\Users\User\Desktop\nitkkr2.jpg"]
        
        # Load the first image
        self.current_image_index = 0
        self.load_image()
        
        # Start a timer to change images
        self.root.after(1000, self.change_image)
        
    def load_image(self):
        # Load image from the current index
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((1000, 300))
        self.photo = ImageTk.PhotoImage(image)
        
        # Display the image on a label
        self.label = Label(self.main_frame_image, image=self.photo)
        self.label.place(x=0,y=0,height=650,width=635)
        
    def change_image(self):
        # Change to the next image
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_image()
        
        # Reset the timer
        self.root.after(1000, self.change_image)
 
        img_frame_label = Label(self.main_frame_image, text="60 YEARS OF EXCELLENCE AND DEDICATION!", font=("comic sans ms", 17, "bold"), fg="white", bg="#77B0AA",relief=SUNKEN)
        img_frame_label.place(x=0, y=0, width=635, height=170)
    
    def go_to_home_page(self):
    # Close the current window
        self.destroy()
        
        # Show the home page again
        self.home_page.update()
        self.home_page.deiconify()
 
       
 
if __name__=="__main__":
    root=Tk()
    obj = About_us(root)
    root.mainloop()
