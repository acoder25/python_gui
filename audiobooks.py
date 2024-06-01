from tkinter import*
from tkinter import filedialog
import random
from PIL import ImageTk, Image
import sqlite3
import os
 
class my_audios():
    def __init__(self,root):
        self.root=root
        self.root.title("AUDIOBOOKS")
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
        side_frame.place(x=0,y=122,height=680,width=258.33)
        my_button5=Button(side_frame,text="SWITCH ACCOUNT",fg="white",bg="#382b58",font=("comic sans ms", 15, "bold"),
                    relief="raised",command=logout)
        my_button5.place(x=0,y=620,height=50,width=258.33)
 
        lbl_title=Label(root,text="AUDIOBOOKS",font=("comic sans ms",18,"bold"),bg="#382b58",fg="white")
        lbl_title.place(x=0,y=120,width=1550,height=50)
 
        #mid frame for audiobooks//>
 
        label_frame_mid=LabelFrame(self.root,bd=2,relief=RIDGE,text="LISTEN UP-Tune into Audiobooks!",font=("comic sans ms", 19, "bold"))
        label_frame_mid.place(x=258.33,y=170,width=1400,height=630)
 
        # Connect to the SQLite database
        conn = sqlite3.connect('audiobooks.db')
        cursor = conn.cursor()
 
        # Fetch book data from the database
        cursor.execute("SELECT name, audio_path, image_path FROM audiobooks")
        audiobooks = cursor.fetchall()
 
        # Close the database connection
        conn.close()
 
        # Function to open PDF file
        def open_audio(audio_path):
            try:
                os.startfile(audio_path)
            except OSError:
                # Handle error if PDF file cannot be opened
                tk.messagebox.showerror("Error", "Unable to open AUDIO file.")
 
        # Loop through the books and display them
        audiobooks1=audiobooks[0:2]
        for audiobook in range(len(audiobooks1)):
            name, audio_path, image_path = audiobooks1[audiobook]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img2 = I1.resize((200, 250))
            my_img2 = ImageTk.PhotoImage(new_img2)
            cover_label1 = Label(label_frame_mid, image=my_img2)
            cover_label1.image=my_img2
            cover_label1.grid(row=audiobook,column=0,pady=20,padx=20)
 
    
            # Create a button to open the PDF file
            audio_button = Button(label_frame_mid, text="PLAY CLIP", command=lambda path=audio_path: open_audio(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            audio_button.grid(row=audiobook,column=1)
 
            audiobooks2=audiobooks[2:4]
        for audiobook in range(len(audiobooks2)):
            name, audio_path, image_path = audiobooks2[audiobook]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img2 = I1.resize((200, 250))
            my_img2 = ImageTk.PhotoImage(new_img2)
            cover_label1 = Label(label_frame_mid, image=my_img2)
            cover_label1.image=my_img2
            cover_label1.grid(row=audiobook,column=3,pady=20,padx=20)
 
    
            # Create a button to open the PDF file
            audio_button = Button(label_frame_mid, text="PLAY CLIP", command=lambda path=audio_path: open_audio(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            audio_button.grid(row=audiobook,column=4)
 
            audiobooks3=audiobooks[4:6]
        for audiobook in range(len(audiobooks3)):
            name, audio_path, image_path = audiobooks3[audiobook]
 
            # Load the book cover image
            I1 = Image.open(image_path)
            new_img2 = I1.resize((200, 250))
            my_img2 = ImageTk.PhotoImage(new_img2)
            cover_label1 = Label(label_frame_mid, image=my_img2)
            cover_label1.image=my_img2
            cover_label1.grid(row=audiobook,column=5,pady=20,padx=20)
 
    
            # Create a button to open the PDF file
            audio_button = Button(label_frame_mid, text="PLAY CLIP", command=lambda path=audio_path: open_audio(path),bg="#77B0AA",fg="black",font=("comic sans ms", 15, "bold"),relief="raised")
            audio_button.grid(row=audiobook,column=6)
 
if __name__=="__main__":
    root=Tk()
    obj=my_audios(root)
    root.mainloop()
