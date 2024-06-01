
from tkinter import*
from tkinter import filedialog
import random
from PIL import ImageTk, Image
import sqlite3
import os
 
class my_notification():
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
        side_frame=Frame(root,bd=4,relief="raised",bg="#382b58")
        side_frame.place(x=0,y=170,height=680,width=258.33)
        my_button5=Button(side_frame,text="SWITCH ACCOUNT",fg="white",bg="#382b58",font=("comic sans ms", 15, "bold"),
                    relief="raised",command=self.logout)
        my_button5.place(x=0,y=620,height=50,width=258.33)
 
        lbl_title=Label(root,text="NOTIFICATIONS",font=("comic sans ms",18,"bold"),bg="#382b58",fg="white")
        lbl_title.place(x=0,y=120,width=1550,height=50)
 
        # mid frame for books
        label_frame_mid=LabelFrame(self.root,bd=2,relief=RIDGE,text="CHECK!!",font=("comic sans ms", 19, "bold"),bg="#77B0AA")
        label_frame_mid.place(x=550,y=250,width=700,height=500)
 
 
        # setting notification1 and popup window1
        self.popup_open = False
 
        # Create a notification label1
        notification_label = Label(label_frame_mid, text="->Library Closures",font=("comic sans ms",18,"bold"))
        notification_label.place(x=100,y=50)
 
        # Bind the hover event to the notification label
        notification_label.bind("<Enter>", self.show_popup)
 
        #setting notification 2 and pop up window 2//>
 
        # Create a notification label2
        notification_label = Label(label_frame_mid, text="->Due Date Renewal",font=("comic sans ms",18,"bold"))
        notification_label.place(x=100,y=130)
 
        # Bind the hover event to the notification label
        notification_label.bind("<Enter>", self.show_popup1)
 
        #setting notification 3 and pop up window 3//>
 
        # Create a notification label3
        notification_label = Label(label_frame_mid, text="->New Arrival",font=("comic sans ms",18,"bold"))
        notification_label.place(x=100,y=210)
 
        # Bind the hover event to the notification label
        notification_label.bind("<Enter>", self.show_popup2)
 
        #setting notification 4 and pop up window 4//>
 
        # Create a notification label4
        notification_label = Label(label_frame_mid, text="->New Library Timings",font=("comic sans ms",18,"bold"))
        notification_label.place(x=100,y=290)
 
        # Bind the hover event to the notification label
        notification_label.bind("<Enter>", self.show_popup3)
 
    def logout(self):
        # Close the current window
        self.root.destroy()
        # Open the login page window or frame
        self.open_login_page()
 
    def open_login_page(self):
        login_root = Tk()
        login_root.title("login form")
        login_root.geometry("1550x800+0+0")
        login_root.iconbitmap(r"C:\Users\User\Desktop\lib_icon.png")
        login_root.mainloop()
 
    def show_popup(self, event):
        # Check if popup is already open, if yes, return
        if self.popup_open:
            return
        
        # Get the position of the mouse cursor
        x, y = event.x_root, event.y_root
 
        # Create a popup window
        popup = Toplevel(self.root)
        popup.geometry(f"400x200+{x}+{y}")
        popup.title("Notification Details")
        
        # Set flag to indicate popup is open
        self.popup_open = True
 
        # Add content to the popup
        details_label = Label(popup, text="NIT KURUKSHETRA\n LIBRARY MANAGEMENT\n All the students are hereby informed that the\n library will remain closed on 29-04-2024(Monday)\n due to maintenace reasons.\n Renewal and Issuing of books is debarded.",font=("comic sans ms", 13, "bold"),bg="#DAC0A3")
 
        details_label.pack(pady=15)
        
        # Bind the popup window to close when mouse leaves
        popup.bind("<Leave>", lambda event: self.close_popup(popup))
 
    def show_popup1(self, event):
        # Check if popup is already open, if yes, return
        if self.popup_open:
            return
        
        # Get the position of the mouse cursor
        x, y = event.x_root, event.y_root
 
        # Create a popup window
        popup = Toplevel(self.root)
        popup.geometry(f"400x200+{x}+{y}")
        popup.title("Notification Details")
        
        # Set flag to indicate popup is open
        self.popup_open = True
 
        # Add content to the popup
        details_label = Label(popup, text="NIT KURUKSHETRA\n LIBRARY MANAGEMENT\n All the students are hereby requested\n to clear all their dues and fines of the\n issued books by 30-04-2024(Tuesday).",font=("comic sans ms", 13, "bold"),bg="#DAC0A3")
 
        details_label.pack(pady=15)
        
        # Bind the popup window to close when mouse leaves
        popup.bind("<Leave>", lambda event: self.close_popup(popup))
 
    def show_popup2(self, event):
        # Check if popup is already open, if yes, return
        if self.popup_open:
            return
        
        # Get the position of the mouse cursor
        x, y = event.x_root, event.y_root
 
        # Create a popup window
        popup = Toplevel(self.root)
        popup.geometry(f"400x200+{x}+{y}")
        popup.title("Notification Details")
        
        # Set flag to indicate popup is open
        self.popup_open = True
 
        # Add content to the popup
        details_label = Label(popup, text="NIT KURUKSHETRA\n LIBRARY MANAGEMENT\n All the students are hereby notified\n about new books, journals, or other\n study materials added to the library's\n collection.",font=("comic sans ms", 13, "bold"),bg="#DAC0A3")
 
        details_label.pack(pady=15)
        
        # Bind the popup window to close when mouse leaves
        popup.bind("<Leave>", lambda event: self.close_popup(popup))
 
    def show_popup3(self, event):
    # Check if popup is already open, if yes, return
        if self.popup_open:
            return
        
        # Get the position of the mouse cursor
        x, y = event.x_root, event.y_root
 
        # Create a popup window
        popup = Toplevel(self.root)
        popup.geometry(f"400x200+{x}+{y}")
        popup.title("Notification Details")
        
        # Set flag to indicate popup is open
        self.popup_open = True
 
        # Add content to the popup
        details_label = Label(popup, text="NIT KURUKSHETRA\n LIBRARY MANAGEMENT\n All the students are hereby notified\n about the change in library timings.\nThe library timings for issuing books and\n reading is modified to 10 am to 6pm for\n the students.",font=("comic sans ms", 13, "bold"),bg="#DAC0A3")
 
        details_label.pack(pady=10)
        
        # Bind the popup window to close when mouse leaves
        popup.bind("<Leave>", lambda event: self.close_popup(popup))    
 
    def close_popup(self, popup):
        # Destroy the popup window
        popup.destroy()
        
        # Set flag to indicate popup is closed
        self.popup_open = False
 
if __name__=="__main__":
    root=Tk()
    obj=my_notification(root)
    root.mainloop()
