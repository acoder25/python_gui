from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox
from tkinter import Scrollbar 
from tkinter import filedialog

class Profile_sub:
	def __init__(self, root):
			self.root = root
			self.root.title("PROFILE")
			self.root.geometry("1550x800+0+0")
			# logo
			I1 = Image.open(r"C:\Users\User\Desktop\logo.png")
			new_img1 = I1.resize((120, 120))
			my_img1 = ImageTk.PhotoImage(new_img1)
			l2 = Label(root, image=my_img1)
			l2.place(x=0, y=0)

			def upload():
		    # Open file dialog to select an image file
			    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
			    if file_path:
			        	conn = sqlite3.connect("admin_image.db")
			        	c = conn.cursor()
			        	c.execute("DELETE FROM admin_imgs")
			        	c.execute("INSERT INTO admin_imgs VALUES (:var_image)",
					              {
					                  'var_image': r"{}".format(file_path),
					              })
			        	conn.commit()
			        	conn.close()


			        	
			def update():
				root = Tk()
				root.title("UPDATE INFO")
				root.geometry("700x700+500+70")
				connection = sqlite3.connect("admin.db")
				cursor = connection.cursor()
				


				connection.commit()

				# Close the connection
				connection.close()

				def save():
					connection = sqlite3.connect("admin.db")
					cursor = connection.cursor()
					cursor.execute("DELETE FROM admins")


					# Execute SQL command to delete records
					# cursor.execute("DELETE FROM admins")
					cursor.execute("INSERT INTO admins VALUES (:var_name, :var_id)",
					  {
					      'var_name': entry20.get(),
					      'var_id': entry21.get()
					      
					  })
					connection.commit()
					connection.close()
					root.destroy()

				big_frame=Frame(root,bd=4,relief="raised",background="#D24545")
				big_frame.place(x=50,y=50,width=600,height=600)


				up_label=Label(big_frame,text="UPDATE INFO",background="#C0D6E8",font=("comic sans ms",20,"bold"))
				up_label.place(x=50,y=50,width=500,height=100)

				small_frame=Frame(big_frame,bd=4,relief="raised",background="#C5EBAA")
				small_frame.place(x=50,y=150,width=500,height=300)

				l20=Label(small_frame,text="NAME:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l20.place(x=30,y=80)

				entry20=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry20.place(x=110,y=80)

				l21=Label(small_frame,text="ID:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l21.place(x=30,y=150)

				entry21=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry21.place(x=110,y=150)

				my_button1 = Button(small_frame, text="SAVE", padx=20, pady=10,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=save)
				my_button1.place(x=80,y=200)


				root.mainloop()


			def logout():
				root.destroy()
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

			lbl_title = Label(root, text="LIBRARY MANAGMENT SYSTEM", font=("comic sans ms", 20, "bold"), fg="white", bg="#007F73")
			lbl_title.place(x=120, y=0, width=1550, height=120)

			lb1 = Label(root, text="PROFILE", font=("comic sans ms", 20, "bold"), fg="white", bg="#382b58")
			lb1.place(x=0, y=120, width=1550, height=80)

			side_frame=Frame(root,bd=4,relief="raised",bg="#007F73")
			side_frame.place(x=0,y=200,height=600,width=250)

			b2=Button(side_frame,text="SWITCH ACCOUNT",background="#007F73",fg="black",font=("comic sans ms", 15, "bold"),relief="raised",bd=2,command=logout)
			b2.place(x=0,y=530,width=258.33,height=50)

			main_frame=Frame(root,bd=4,relief="raised")
			main_frame.place(x=260,y=210,height=590,width=1250)

			conn=sqlite3.connect("admin_image.db")
			c=conn.cursor()
			c.execute("SELECT * FROM admin_imgs")
			image_paths=c.fetchall()
			image_path=image_paths[0][0]
			print(image_path)

			I2 = Image.open(image_path)
			new_img2 = I2.resize((250, 250))
			my_img2 = ImageTk.PhotoImage(new_img2)
			l200 = Label(main_frame, image=my_img2)
			l200.place(x=150, y=50)

			details_frame=Frame(main_frame,bd=5,relief="raised",background="#C5EBAA")
			details_frame.place(x=600,y=40,height=520,width=550)

			conn=sqlite3.connect("admin.db")
			c=conn.cursor()
			c.execute("SELECT name FROM admins")

			rows=c.fetchall()
			row=rows[0][0]

			l10=Label(details_frame,text="NAME:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l10.place(x=30,y=80)


			l101=Label(details_frame,text=row,font=("comic sans ms",17,"bold"),background="#C5EBAA")
			l101.place(x=200,y=80)

			c.execute("SELECT id from admins")

			row1=c.fetchall()
			l11=Label(details_frame,text="ID:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l11.place(x=30,y=130)


			l102=Label(details_frame,text=row1,font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l102.place(x=200,y=130)

			conn.commit()

			conn.close()

			l101=Label(details_frame,text="CONTACT:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l101.place(x=30,y=180)


			l103=Label(details_frame,text="+01744-233208" ,font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l103.place(x=200,y=180)

			l101=Label(details_frame,text="MAIL ID:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l101.place(x=30,y=230)


			l104=Label(details_frame,text="library_admin@nitkkr.ac.in",font=("comic sans ms",15,"bold"),background="#C5EBAA")
			l104.place(x=200,y=230)

			my_button = Button(details_frame, text="UPDATE", padx=20, pady=10,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=update)
			my_button.place(x=100,y=400)

			my_button100 = Button(main_frame, text="UPLOAD", padx=20, pady=10,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=upload)
			my_button100.place(x=200,y=350)




			self.root.mainloop()

if __name__=="__main__":

	root=Tk()
	obj = Profile_sub(root)
	root.mainloop()

       
