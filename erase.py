from tkinter import *
from PIL import ImageTk,ImageTk
import sqlite3


root=Tk()
root.title("database")
root.geometry("4000x400")

def clear_records():
    try:
        # Connect to the database
        connection = sqlite3.connect("student.db")
        cursor = connection.cursor()
        
        # Execute SQL command to delete records
        cursor.execute("DELETE FROM stus")
        
        # Commit the changes
        connection.commit()
        
        # Close the connection
        connection.close()
        
        # Notify the user that records have been cleared
        
    except sqlite3.Error as error:
        # Handle any errors that occur
        status_label.config(text=f"Error: {error}", fg="red")
conn=sqlite3.connect("selected_student.db")

c=conn.cursor()

c.execute("""CREATE TABLE sel_students(
           name text,
           roll int,
           books text,
           year int,
           idate text,
           fine int
           
	       )""")
c.execute("""CREATE TABLE admins (
             
             name text,
             id int

            )""")
c.execute("INSERT INTO sel_students VALUES(:var_name,:var_roll,:var_books,:var_year,:var_idate,:var_fine)",{

          'var_name':"Ayush Pandey",
          'var_roll':123109084,
          'var_books':"B.S grewal",
          'var_year':2,
          'var_idate':"04-20-2024",
          'var_fine':10



    })



c.execute("INSERT INTO admins VALUES (:var_name,:var_id)",
          {
              'var_name':"Aryan kumar",
              'var_id':256
              
              
              
          })

c.execute('SELECT * FROM stus')
column_names = [desc[0] for desc in c.description]
print("Column Names:", ', '.join(column_names))

conn.commit()

conn.close()
root.mainloop()
