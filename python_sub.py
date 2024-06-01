from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox
from datetime import datetime
from datetime import date
from tkcalendar import DateEntry


class Stu_corner:

    def __init__(self,root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

        #variables
        self.var_fine=StringVar()
        x=random.randint(10,1000)
        self.var_fine.set(str(x))

        def update():

            # Get student name from entry field
            student_name = entry_ref.get()

            # Validate user input (optional)
            if not student_name:
                message_label.config(text="Please enter a student name!", fg="red")
                return

            # Connect to the database
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()

            # Create select query to find student (replace 'books' with your table name if different)
            select_query = f"SELECT * FROM stus WHERE name = ?"

            selected_date =datetime.strptime(cal.get(), "%m/%d/%y")
            x=datetime.now()-selected_date
            z=x.days-14
            y=0
            conn1=sqlite3.connect("fine.db")
            c1=conn1.cursor()
            c1.execute("SELECT fine FROM fines")
            rows=c1.fetchall()
            row=rows[0][0]
            if z>0:
                y=z*row

            conn1.commit()
            conn1.close() 

            # Execute select query with parameter
            try:
                cursor.execute(select_query, (student_name,))
                data = cursor.fetchone()

                if not data:
                    message_label.config(text=f"Student '{student_name}' not found!", fg="red")
                    return

                # Get updated student information from entry fields
                # Assuming roll_no and books_issued are editable, modify as needed
                name = entry_ref.get()
                roll= entry_ref2.get()  # Assuming roll_no is editable now
                book= entry_ref3.get()
                year=year_menu.get()
                idate=cal.get()
                fine=y

                # Create update query
                update_query = f"""
                UPDATE stus
                SET name = ?, roll= ?, book= ?,year=?,idate=?,fine=?
                WHERE name = ?
                """

                # Execute update query with parameters
                cursor.execute(update_query, (name, roll, book,year,idate,fine, student_name))
                conn.commit()
                conn.close()
                entry_ref.delete(0,END)
                entry_ref2.delete(0,END)
                entry_ref3.delete(0,END)
                entry_ref4.delete(0,END)
                year_menu.delete(0,END)
                cal.delete(0,END)
               

                # Update treeview (optional, can be called from populate_treeview)
                # ... (code to update treeview based on updated data)
            
            finally:
                conn.close()  # Ensure connection is closed even on exceptions



        

        def submit():
           

           conn = sqlite3.connect("student.db")
           c = conn.cursor()
           selected_date =datetime.strptime(cal.get(), "%m/%d/%y")
           x=datetime.now()-selected_date
           z=x.days-14
           y=0
           conn1=sqlite3.connect("fine.db")
           c1=conn1.cursor()
           c1.execute("SELECT fine FROM fines")
           rows=c1.fetchall()
           row=rows[0][0]
           if z>0:
            y=z*row

           conn1.commit()
           conn1.close() 


           c.execute("INSERT INTO stus VALUES (:var_name, :var_roll, :var_books, :var_year,:var_date,:var_fine)",
          {
              'var_name': entry_ref.get(),
              'var_roll': entry_ref2.get(),
              'var_books': entry_ref3.get(),
              'var_year': year_menu.get(),
              
              'var_date':cal.get(),
              'var_fine':y


          })

           conn.commit()
           conn.close()
           entry_ref.delete(0,END)
           entry_ref2.delete(0,END)
           entry_ref3.delete(0,END)
           entry_ref4.delete(0,END)
           year_menu.delete(0,END)
           cal.delete(0,END)



        def query():
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("student.db")
            c = conn.cursor()
            c.execute("SELECT * FROM stus")
            records = c.fetchall()
            tree.tag_configure("oddrow", background="#FBF8DD")
            tree.tag_configure("evenrow", background="#8DECB4")
            for i, row in enumerate(records):
                
                name , roll, book, year, idate, fine = row
                # Load image (replace 'image' with column name from your data)
                

                # Insert data with tag based on row index (odd or even)
                if i % 2 == 0:  # Even row
                    tree.insert("", "end", values=( name , roll, book, year, idate, fine), tags=("evenrow",))
                else:  # Odd row
                    tree.insert("", "end", values=(name , roll, book, year, idate, fine), tags=("oddrow",))

                
            
            

            conn.commit()
            conn.close()
           
  
        I2 = Image.open(r"C:\Users\User\Desktop\logo.png")
        new_img2 = I2.resize((120, 80))
        my_img2 = ImageTk.PhotoImage(new_img2)
        lb101 = Label(root, image=my_img2)
        lb101.image = my_img2  # Keep a reference to the image object
        lb101.place(x=0, y=0)

        
        lbl_title=Label(root,text="LIBRARY MANAGMENT SYSTEM",font=("comic sans ms",20,"bold"),fg="white",bg="#007F73")
        lbl_title.place(x=120,y=0,width=1550,height=120)
        
        l2=Label(root,text="STUDENT'S DETAILS",font=("comic sans ms",18,"bold"),fg="white",background="#382b58")
        l2.place(x=0,y=80,height=60,width=1550)
        
        label_add=Label(root,relief="ridge", font=("pacifico",10,"bold"),bg="#007F73")

        l3=Label(label_add,text="NEW ENTRY",font=("Courier New",20,"bold"),bg="#007F73")
        label_add.place(x=0,y=140,height=660,width=300)
        l3.place(x=70,y=50)
        
        lb1=Label(label_add,text="NAME:",font=("Courier New",14,"bold"),bg="#007F73")
        lb1.place(x=20,y=100)
        
        entry_ref=ttk.Entry(label_add,font=("Lucida Bright",12))
        entry_ref.place(x=100,y=100)

        lbl2=Label(label_add,text="ROLL NO:",font=("Courier New",14,"bold"),bg="#007F73")
        lbl2.place(x=15,y=150)
        
        entry_ref2=ttk.Entry(label_add,font=("Lucida Bright",12))
        entry_ref2.place(x=100,y=150)
        

        lbl3=Label(label_add,text="TITLE:",font=("Courier New",14,"bold"),bg="#007F73")
        lbl3.place(x=20,y=200)
        
        entry_ref3=ttk.Entry(label_add,font=("Lucida Bright",12))
        entry_ref3.place(x=100,y=200)
        

        lbl4=Label(label_add,text="ISBN:",font=("Courier New",14,"bold"),bg="#007F73")
        lbl4.place(x=20,y=250)
        
        entry_ref4=ttk.Entry(label_add,font=("Lucida Bright",12))
        entry_ref4.place(x=100,y=250)
        
        lbln=Label(label_add,text="YEAR:",font=("Courier New",14,"bold"),bg="#007F73")
        lbln.place(x=20,y=300)
        style = ttk.Style()
        style.theme_use('vista')

        style.configure('TButton', font=('Helvetica', 12))

        style.configure('TCombobox', font=('Helvetica', 12))


        year_var = StringVar(root)
        year_var.set("1st Year")  # Default selection

# Create a dropdown menu with custom styling
        year_menu = ttk.Combobox(label_add, values=["1st Year", "2nd Year", "3rd Year", "4th Year"], width=15)
        year_menu.place(x=100,y=300)

        lbld=Label(label_add,text="DATE:",font=("Courier New",14,"bold"),bg="#007F73")
        lbld.place(x=20,y=350)

        cal = DateEntry(label_add, width=12, background="darkblue", foreground="white", borderwidth=2)
        cal.place(x=100,y=350)

        details_table=Frame(root,bd=2,relief="raised")
        details_table.place(x=300,y=140,height=660,width=1230)

        style = ttk.Style()
        style.configure("mystyle.Treeview", rowheight=70, font=("comic sans ms", 12))
        style.configure("mystyle.Treeview.Heading", font=("Times New Roman", 16), anchor=CENTER,background="#FFC94A")  # Style for headings
        style.configure("mystyle.Treeview.Row", anchor=CENTER)  # Style for rows (optional)


        tree = ttk.Treeview(details_table, show="headings", style="mystyle.Treeview")
        tree["columns"] = ("NAME", "ROLL NO", "BOOK", "YEAR", "ISSUE DATE", "FINE")

# Define column headings
        
        tree.heading("NAME", text="NAME", anchor=CENTER)
        tree.heading("ROLL NO", text="ROLL NO", anchor=CENTER)
        tree.heading("BOOK", text="BOOK",anchor=CENTER)
        tree.heading("YEAR", text="YEAR", anchor=CENTER)
        tree.heading("ISSUE DATE", text="ISSUE DATE", anchor=CENTER)
        tree.heading("FINE", text="FINE",anchor=CENTER)
        


        
        tree.column("NAME", anchor=CENTER, width=150)
        tree.column("ROLL NO", anchor=CENTER, width=100)
        tree.column("BOOK",anchor=CENTER, width=100)
        tree.column("YEAR",anchor=CENTER, width=80)
        tree.column("ISSUE DATE",anchor=CENTER, width=80)
        tree.column("FINE",anchor=CENTER, width=80)
        

        # Populate the treeview with data from the database
        

        # Pack the treeview
        tree.pack(expand=True, fill="both")

        my_button = Button(label_add, text="ADD", padx=20, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=submit)
        my_button.place(x=40,y=430)

        my_button2 = Button(label_add, text="FETCH", padx=10, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=query)
        my_button2.place(x=150,y=430)

        my_button3 = Button(label_add, text="UPDATE", padx=10, pady=5,fg="white", background="black",font=("Courier",15,"bold"),relief="raised",command=update)
        my_button3.place(x=100,y=500)




       


if __name__=="__main__":
    root=Tk()
    obj = Stu_corner(root)
    root.mainloop()

        

       

