from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox
from tkinter import filedialog

class Catalog:
	def __init__(self, root):
		self.root = root
		self.root.title("LIBRARY MANAGEMENT SYSTEM")
		self.root.geometry("1550x800+0+0")

		def update():
			# Get student name and ISBN from entry fields
		    student_name = entry_ref.get()
		    isbn = entry_ref2.get()

		    # Validate user input (optional)
		    if not student_name or not isbn:
		        message_label.config(text="Please fill in all fields!", fg="red")
		        return

		    # Connect to the database
		    conn = sqlite3.connect("avl_books.db")
		    cursor = conn.cursor()

		    # Create select query to find student (replace 'books' with your table name if different)
		    select_query = f"SELECT * FROM dbooks WHERE name = ? AND isbn = ?"

		    # Execute select query with parameters
		    try:
		        cursor.execute(select_query, (student_name, isbn))
		        data = cursor.fetchone()

		        if not data:
		            message_label.config(text=f"Student '{student_name}' with ISBN '{isbn}' not found!", fg="red")
		            return

		        # Get updated student name (assuming ISBN doesn't change)
		        updated_name = entry_ref.get()

		        # Create update query (replace 'books' with your table name if different)
		        # Keep existing image path by not modifying the image column (if applicable)
		        update_query = f"""
		        UPDATE dbooks
		        SET name = ?, author = ?, totalcpy = ?, leftcpy = ?
		        WHERE name = ? AND isbn = ?
		        """

		        # Get potentially updated author, total copy, and left copy values (optional)
		        author = entry_ref3.get()  # Check for entry existence
		        totalcpy = entry_ref4.get() 
		        leftcpy = entry_ref5.get() 

		        # Execute update query with parameters
		        cursor.execute(update_query, (updated_name, author, totalcpy, leftcpy, student_name, isbn))
		        conn.commit()
		       

		        # Optional: Update treeview after successful update (consider calling populate_treeview)
		        # ...

		    except sqlite3.Error as err:
		        message_label.config(text=f"Error updating record: {err}", fg="red")

		    finally:
		        conn.close()  # Ensure connection is closed even on exceptions

		
		def select_image():
		    # Open file dialog to select an image file
		    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
		    if file_path:
		        try:
		        	return file_path

		            

		        except sqlite3.Error as error:
		            # Handle any errors that occur
		            print("Unsuccessful")

		def load_image(image_path, width, height):
			# image109 = Image.open(r"{path}".format(path=image_path))
			image109 = Image.open(image_path)
			image109 = image109.resize((width,height), Image.ANTIALIAS)
			return ImageTk.PhotoImage(image109)

		def populate_tree(tree):
			tree.delete(*tree.get_children())

			# Connect to the database

			connection = sqlite3.connect("avl_books.db")

			cursor = connection.cursor()


			# Execute SQL query to select book information

			cursor.execute("SELECT name, isbn, author, totalcpy, leftcpy, image FROM dbooks")


			# Fetch all rows

			rows = cursor.fetchall()
			tree.tag_configure("oddrow", background="#FBF8DD")
			tree.tag_configure("evenrow", background="#C0D6E8")



			# Insert data into the treeview
			j=0
			# for row in rows:
			# 	i+=1

			# 	name, isbn, author, totalcpy, leftcpy, image = row


			# 	# Load the book cover image

			# 	book_cover = load_image(image, 50, 70)


			# 	# Insert data into the treeview

			# 	tree.insert("", "end", values=(name,isbn, author, totalcpy, leftcpy))


			# 	# Create a label to display the image

			# 	label = Label(tree, image=book_cover)
			# 	label.image = book_cover
			# 	label.place(x=470, y=-220+130*(i-1), in_=tree, relx=0.5, rely=0.5, anchor=CENTER)
			# 	# Close the connection

			# connection.close()
			for i, row in enumerate(rows):
				j+=1
				name, isbn, author, totalcpy, leftcpy, image = row
				# Load image (replace 'image' with column name from your data)
				book_cover = load_image(image, 50, 70)

				# Insert data with tag based on row index (odd or even)
				if i % 2 == 0:  # Even row
				    tree.insert("", "end", values=( name, isbn, author, totalcpy, leftcpy), tags=("evenrow",))
				else:  # Odd row
				    tree.insert("", "end", values=(name, isbn, author, totalcpy, leftcpy), tags=("oddrow",))

				label = Label(tree, image=book_cover)
				label.image = book_cover
				label.place(x=470, y=-220+100*(j-1), in_=tree, relx=0.5, rely=0.5, anchor=CENTER)
				# Close the connection
			connection.close()



		def submit():
		   

		   conn = sqlite3.connect("avl_books.db")
		   c = conn.cursor()

		   c.execute("INSERT INTO dbooks VALUES (:var_name, :var_isbn, :var_author, :var_total,:var_left,:var_image)",
		  {
		      'var_name': entry_ref.get(),
		      'var_isbn': entry_ref2.get(),
		      'var_author':entry_ref3.get(),
		      'var_total': entry_ref4.get(),
		      'var_left':entry_ref5.get(),
		      'var_image':select_image()

		      
		  })

		   conn.commit()
		   conn.close()
		   entry_ref.delete(0,END)
		   entry_ref2.delete(0,END)
		   entry_ref3.delete(0,END)
		   entry_ref4.delete(0,END)
		   entry_ref5.delete(0,END)

		def query():
		   
		    conn = sqlite3.connect("avl_books.db")
		    c = conn.cursor()
		    c.execute("SELECT image FROM dbooks")
		    records = c.fetchall()
		    populate_tree(tree)
		    




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

		lbl_title = Label(root, text="LIBRARY MANAGMENT SYSTEM", font=("comic sans ms", 20, "bold"), fg="white", bg="#007F73")
		lbl_title.place(x=120, y=0, width=1550, height=120)

		lb1 = Label(root, text="CATALOG MANAGEMENT", font=("comic sans ms", 20, "bold"), fg="white", bg="#382b58")
		lb1.place(x=0, y=120, width=1550, height=80)

		label_add=Label(root,relief="ridge", font=("pacifico",10,"bold"),bg="#007F73")
		label_add.place(x=0,y=200,height=660,width=300)

		l3=Label(label_add,text="BOOK DETAILS",font=("comic sans ms",20,"bold"),bg="#007F73")
		
		l3.place(x=40,y=30)

		lb1=Label(label_add,text="NAME:",font=("pacifico",14,"bold"),bg="#007F73")
		lb1.place(x=15,y=100)

		entry_ref=ttk.Entry(label_add,font=("Lucida Bright",12))
		entry_ref.place(x=130,y=100,width=150)

		lbl2=Label(label_add,text="ISBN:",font=("pacifico",14,"bold"),bg="#007F73")
		lbl2.place(x=15,y=150)

		entry_ref2=ttk.Entry(label_add,font=("Lucida Bright",12))
		entry_ref2.place(x=130,y=150,width=150)


		lbl3=Label(label_add,text="AUTHOR:",font=("pacifico",14,"bold"),bg="#007F73")
		lbl3.place(x=15,y=200)

		entry_ref3=ttk.Entry(label_add,font=("Lucida Bright",12))
		entry_ref3.place(x=130,y=200,width=150)


		lbl4=Label(label_add,text="TOTAL CPY:",font=("pacifico",14,"bold"),bg="#007F73")
		lbl4.place(x=13,y=250)

		entry_ref4=ttk.Entry(label_add,font=("Lucida Bright",12))
		entry_ref4.place(x=150,y=250,width=100)

		lbln=Label(label_add,text="LEFT CPY:",font=("pacifico",14,"bold"), bg="#007F73")
		lbln.place(x=15,y=300)

		entry_ref5=ttk.Entry(label_add,font=("Lucida Bright",12))
		entry_ref5.place(x=150,y=300,width=100)

		# select_button = Button(label_add, text="IMAGE", command=select_image,bg="black",fg="white",font=("Courier",15,"bold"),relief="raised",padx=20,pady=5)
		# select_button.place(x=50,y=350)

		my_button = Button(label_add, text="ADD", padx=10, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=submit)
		my_button.place(x=40,y=370)

		my_button2 = Button(label_add, text="FETCH", padx=10, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=query)
		my_button2.place(x=150,y=370)

		my_button2 = Button(label_add, text="UPDATE", padx=10, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=update)
		my_button2.place(x=80,y=440)

		main_frame = Frame(root, bd=2, relief="raised")
		main_frame.place(x=300,y=200,height=600,width=1250)

		style = ttk.Style()
		style.configure("mystyle.Treeview", rowheight=100, font=("comic sans ms", 12))
		style.configure("mystyle.Treeview.Heading", font=("Times New Roman", 16), anchor=CENTER,background="#FFC94A")  # Style for headings
		style.configure("mystyle.Treeview.Row", anchor=CENTER)  # Style for rows (optional)


		tree = ttk.Treeview(main_frame, show="headings", style="mystyle.Treeview")
		tree["columns"] = ("Name", "ISBN", "Author", "Total Copy", "Left Copy", "Image")

# Define column headings
        
		tree.heading("Name", text="NAME", anchor=CENTER)
		tree.heading("ISBN", text="ISBN", anchor=CENTER)
		tree.heading("Author", text="AUTHOR",anchor=CENTER)
		tree.heading("Total Copy", text="Total COPY", anchor=CENTER)
		tree.heading("Left Copy", text="Left Copy", anchor=CENTER)
		tree.heading("Image", text="Image",anchor=CENTER)
		


		
		tree.column("Name", anchor=CENTER, width=150)
		tree.column("ISBN", anchor=CENTER, width=100)
		tree.column("Author",anchor=CENTER, width=100)
		tree.column("Total Copy",anchor=CENTER, width=80)
		tree.column("Left Copy",anchor=CENTER, width=80)
		tree.column("Image",anchor=CENTER, width=80)
		

		# Populate the treeview with data from the database
		

		# Pack the treeview
		tree.pack(expand=True, fill="both")


if __name__=="__main__":
    root=Tk()
    obj = Catalog(root)
    root.mainloop()
