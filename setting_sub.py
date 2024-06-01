from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import filedialog

class Setting:
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

			def edit():
				root = Tk()
				root.title("UPDATE FINE")
				root.geometry("400x400+500+70")
				# connection = sqlite3.connect("fine.db")
				# cursor = connection.cursor()
				# cursor.execute("DELETE FROM fines")


				# connection.commit()

				# # Close the connection
				# connection.close()

				def save():
					connection = sqlite3.connect("fine.db")
					cursor = connection.cursor()


					# Execute SQL command to delete records
					cursor.execute("DELETE FROM fines")
					cursor.execute("INSERT INTO fines VALUES (:var_fine)",
					  {
					      'var_fine': entry200.get()
					      
					  })
					connection.commit()
					connection.close()
					root.destroy()


				up_label=Label(root,text="UPDATE FINE",background="#C0D6E8",font=("comic sans ms",20,"bold"))
				up_label.place(x=0,y=0,width=400,height=100)

				small_frame=Frame(root,bd=4,relief="raised",background="#C5EBAA")
				small_frame.place(x=0,y=100,width=400,height=300)

				l20=Label(small_frame,text="FINE:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l20.place(x=30,y=80)

				entry200=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry200.place(x=110,y=80)


				my_button1 = Button(small_frame, text="SAVE", padx=10, pady=5,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=save)
				my_button1.place(x=80,y=150)


				root.mainloop()

			def edit1():
				root = Tk()
				root.title("UPDATE RETURN PERIOD")
				root.geometry("600x600+500+70")
				# connection = sqlite3.connect("fine.db")
				# cursor = connection.cursor()
				# cursor.execute("DELETE FROM fines")


				# connection.commit()

				# # Close the connection
				# connection.close()

				def save1():
					if(entry201.get()=="" or entry202.get()=="" or entry203.get()==""):
						messagebox.showwarning(title="Warning", message="YOU NEED TO SPECIFY ALL FIELDS.")
						root.destroy()
						edit1()
					connection = sqlite3.connect("return_period.db")
					cursor = connection.cursor()


					# Execute SQL command to delete records
					cursor.execute("DELETE FROM return")
					cursor.execute("INSERT INTO return VALUES (:var_ug,:var_pg,:var_faculty)",
					  {
					      'var_ug': entry201.get(),
			              'var_pg':entry202.get(),
			              'var_faculty':entry203.get()
					      
					  })
					connection.commit()
					connection.close()
					root.destroy()


				up_label=Label(root,text="UPDATE RETURN PERIOD",background="#C0D6E8",font=("comic sans ms",17,"bold"))
				up_label.place(x=100,y=0,width=400,height=100)

				small_frame=Frame(root,bd=4,relief="raised",background="#C5EBAA")
				small_frame.place(x=100,y=100,width=400,height=500)

				l20=Label(small_frame,text="UG:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l20.place(x=30,y=50)

				entry201=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry201.place(x=160,y=50,width=180)

				l21=Label(small_frame,text="PG:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l21.place(x=30,y=100)

				entry202=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry202.place(x=160,y=100,width=180)

				l20=Label(small_frame,text="FACULTY:",font=("comic sans ms",15,"bold"),background="#C5EBAA")
				l20.place(x=30,y=150)

				entry203=Entry(small_frame,font=("comic sans ms",15,"bold"),relief="raised",borderwidth=2)
				entry203.place(x=160,y=150,width=180)


				my_button1 = Button(small_frame, text="SAVE", padx=10, pady=5,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=save1)
				my_button1.place(x=80,y=300)


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

			lb1 = Label(root, text="SETTINGS", font=("comic sans ms", 20, "bold"), fg="white", bg="#382b58")
			lb1.place(x=0, y=120, width=1550, height=80)

			I101 = Image.open(r"C:\Users\User\Desktop\settings.png")
			new_img101 = I101.resize((80, 80))
			my_img101 = ImageTk.PhotoImage(new_img101)
			l2000 = Label(lb1, image=my_img101)
			l2000.place(x=870, y=0)


			side_frame=Frame(root,bd=4,relief="raised",bg="#007F73")
			side_frame.place(x=0,y=200,height=600,width=250)

			b2=Button(side_frame,text="SWITCH ACCOUNT",background="#007F73",fg="black",font=("comic sans ms", 15, "bold"),relief="raised",bd=2,command=logout)
			b2.place(x=0,y=530,width=258.33,height=70)

			main_frame=Frame(root,bd=4,relief="raised")
			main_frame.place(x=260,y=210,height=590,width=1250)


			frame1=Frame(main_frame,bd=4,relief="raised",background="#FFEBB2")
			frame1.place(x=200,y=50,width=800,height=100)

			label101=Label(frame1,text="FINE:",background="#FFEBB2",font=("comic sans ms", 20, "bold"))
			label101.place(x=100,y=20)

			conn=sqlite3.connect("fine.db")
			c=conn.cursor()
			c.execute("SELECT fine FROM fines")

			row=c.fetchall()
			f=row[0][0]
			label102=Label(frame1,text="rupee {} / day".format(f),background="#FFEBB2",font=("comic sans ms", 17))
			label102.place(x=250,y=20)

			conn.commit()

			conn.close()
			my_button100 = Button(frame1, text="EDIT", padx=10, pady=5,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=edit)
			my_button100.place(x=600,y=10)

			frame2=Frame(main_frame,bd=4,relief="raised",background="#41B06E")
			frame2.place(x=200,y=150,width=800,height=200)

			label201=Label(frame2,text="RETURN\nPERIOD:",background="#41B06E",font=("comic sans ms", 20, "bold"))
			label201.place(x=100,y=20)

			frame_over=Frame(frame2,bd=4,relief="raised",background="#FFEBB2")
			frame_over.place(x=350,y=10,width=400,height=150)

			label201a=Label(frame_over,text="UG(days):",background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			label201a.place(x=50,y=20)
			conn=sqlite3.connect("return_period.db")
			c=conn.cursor()
			c.execute("SELECT ug FROM return")
			rows=c.fetchall()
			row=rows[0][0]

			labela1=Label(frame_over,text=row,background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			labela1.place(x=170,y=20)

			label201a=Label(frame_over,text="PG:",background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			label201a.place(x=50,y=60)
			
			c.execute("SELECT pg FROM return")
			rows=c.fetchall()
			row=rows[0][0]

			labela1=Label(frame_over,text=row,background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			labela1.place(x=170,y=60)

			label201a=Label(frame_over,text="FACULTY:",background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			label201a.place(x=50,y=100)
			
			c.execute("SELECT faculty FROM return")
			rows=c.fetchall()
			row=rows[0][0]

			labela1=Label(frame_over,text=row,background="#FFEBB2",font=("comic sans ms", 15, "bold"))
			labela1.place(x=170,y=100)

			my_button101 = Button(frame_over, text="EDIT", padx=10, pady=3,fg="white", background="black",font=("comic sans ms",15,"bold"),relief="raised",command=edit1)
			my_button101.place(x=300,y=80)

			conn.commit()
			conn.close()

			frame3=Frame(main_frame,bd=4,relief="raised",background="#FFEBB2")
			frame3.place(x=200,y=350,width=800,height=200)

			label103=Label(frame3,text="TIMINGS:",background="#FFEBB2",font=("comic sans ms", 20, "bold"))
			label103.place(x=100,y=50)

			frame_over1=Frame(frame3,bd=4,relief="raised",background="#41B06E")
			frame_over1.place(x=350,y=30,width=400,height=100)



			label103=Label(frame_over1,text="WEEKDAYS:  08.30 am to 05:30 pm",background="#41B06E",font=("comic sans ms",15, "bold"))
			label103.place(x=0,y=0)

			label103=Label(frame_over1,text="WEEKENDS:  09.00 am to 05.00 pm",background="#41B06E",font=("comic sans ms", 15, "bold"))
			label103.place(x=0,y=40)







			self.root.mainloop()

if __name__=="__main__":

	root=Tk()
	obj = Setting(root)
	root.mainloop()


