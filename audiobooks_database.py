
import tkinter as tk
from tkinter import messagebox
import sqlite3
 
# Function to create the database table
def create_table():
    conn = sqlite3.connect('audiobooks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS audiobooks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  audio_path TEXT NOT NULL,
                  image_path TEXT NOT NULL)''')
    conn.commit()
    conn.close()
 
#function to clear data from database
def clear():
    conn=sqlite3.connect("audiobooks.db")
    c=conn.cursor()
    c.execute("DELETE FROM audiobooks")
    conn.commit()
    conn.close()
 
# Function to add a new book record to the database
def add_book(name, audio_path, image_path):
    conn = sqlite3.connect('audiobooks.db')
    c = conn.cursor()
    c.execute('''INSERT INTO audiobooks (name, audio_path, image_path)
                 VALUES (?, ?, ?)''', (name, audio_path, image_path))
    conn.commit()
    conn.close()
 
# Function to retrieve all book records from the database
def get_all_books():
    conn = sqlite3.connect('audiobooks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM audiobooks')
    audiobooks = c.fetchall()
    conn.close()
    return audiobooks
 
# Example usage of the functions
def main():
    create_table()
 
    # Add a book record
    add_book('SIDDHARTHA',r"C:\Users\User\Desktop\siddhartha_02_hesse_64kb.mp3",r"C:\Users\User\Desktop\Siddhartha audio book.jpeg" )
    add_book('SECRET GARDEN',r"C:\Users\User\Desktop\Secret_Garden.mp3",r"C:\Users\User\Desktop\Secret_Garden.jpeg" )
    add_book('TOM SAWYER',r"C:\Users\User\Desktop\tom_sawyer3_00_twain_64kb.mp3",r"C:\Users\User\Desktop\Adventures_of_Tom_Sawyer.jpeg" )
    add_book('ADVENTURES OF HUCKLEBERRY_FINN',r"C:\Users\User\Desktop\huckfinn_01_twain_apc_64kb.mp3",r"C:\Users\User\Desktop\Adventure_of_Huckleberry_Finn.jpeg")
    add_book('PRIDE AND PREJUDICE',r"C:\Users\User\Desktop\prideandprejudice_01-03_austen_64kb.mp3",r"C:\Users\User\Desktop\pride.jpeg" )
    add_book('HOUSE TO LET',r"C:\Users\User\Desktop\housetolet_1_dickens_64kb.mp3",r"C:\Users\User\Desktop\house_to_let.jpeg")
    add_book('ADVENTURES OF SHERLOCK HOLMES',r"C:\Users\User\Desktop\adventuresholmes_01_doyle_64kb.mp3",r"C:\Users\User\Desktop\sherlock_holmes.jpeg" )
    
 
    # Retrieve all book records
 
    audiobooks = get_all_books()
    for audiobook in audiobooks:
        print(audiobook)
 
 
if __name__ == "__main__":
    main()
