
import tkinter as tk
from tkinter import messagebox
import sqlite3
 
# Function to create the database table
def create_table():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  pdf_path TEXT NOT NULL,
                  image_path TEXT NOT NULL)''')
    conn.commit()
    conn.close()
 
#function to clear data from database
def clear():
    conn=sqlite3.connect("library.db")
    c=conn.cursor()
    c.execute("DELETE FROM books")
    conn.commit()
    conn.close()
 
# Function to add a new book record to the database
def add_book(name, pdf_path, image_path):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''INSERT INTO books (name, pdf_path, image_path)
                 VALUES (?, ?, ?)''', (name, pdf_path, image_path))
    conn.commit()
    conn.close()
 
# Function to retrieve all book records from the database
def get_all_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    return books
 
# Example usage of the functions
def main():
    create_table()
 
    # Add a book record
    add_book('GENESIS', r"C:\Users\User\Downloads\Genesis.pdf",r"C:\Users\User\Desktop\book1.jpg" )
    add_book('KNOWLEDGE REVEALED', r"C:\Users\User\Downloads\Knowledge-Revealed.pdf",r"C:\Users\User\Desktop\book2.jpg" )
    add_book('MADE A KILLING',r"C:\Users\User\Downloads\Made-A-Killing.pdf" , r"C:\Users\User\Desktop\book4.jpg")
    add_book('28 DAYS', r"C:\Users\User\Downloads\28-Days.pdf", r"C:\Users\User\Desktop\reluctant_door.jpg")
    add_book('FORBIDDEN ROACK AND ROLL', r"C:\Users\User\Downloads\Forbidden-Rock-and-Roll.pdf", r"C:\Users\User\Desktop\forbidden.jpg")
    add_book('DEMON GIRL',r"C:\Users\User\Downloads\The-Demon-Girl.pdf", r"C:\Users\User\Desktop\demon girl.jpg")
    add_book('TIME MACHINE', r"C:\Users\User\Downloads\The-Time-Machine.pdf", r"C:\Users\User\Desktop\time machine.jpg")
    add_book('ALLADIN AND MAGIC LAMP', r"C:\Users\User\Downloads\Aladdin-and-the-Magic-Lamp.pdf", r"C:\Users\User\Desktop\alladin.jpg")
 
    # Retrieve all book records
 
    books = get_all_books()
    for book in books:
        print(book)
 
 
if __name__ == "__main__":
    main()
