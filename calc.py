from tkinter import *

root = Tk()
root.title("simple calculator")
root.configure(background="black")


def button_clear():
    e.delete(0,END)


def button_click(number):
    x = e.get()
    e.delete(0,END)
    current= x + str(number)
    e.insert(0,current)


def button_add():
    first_num= e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)


def button_equal():
    second_num = int(e.get())
    e.delete(0, END)
    if math == "addition":
        x = f_num + second_num
    if math == "subtraction":
        x = f_num - second_num
    if math == "multiplication":
        x = f_num * second_num
    if math == "division":
        x = f_num / second_num
    e.insert(0, str(x))


def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)


e= Entry(root, width=35 ,bd=5 , relief="raised")
e.grid(row=0,column=0,columnspan=3)

b1=Button(root,text="1",padx=25,pady=10,command=lambda: button_click(1))
b1.grid(row=1,column=0)
b2=Button(root,text="2",padx=25,pady=10,command=lambda: button_click(2))
b2.grid(row=1,column=1)
b3=Button(root,text="3",padx=25,pady=10 , command=lambda: button_click(3))
b3.grid(row=1,column=2)

b4=Button(root,text="4",padx=25,pady=10,command=lambda: button_click(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",padx=25,pady=10 ,command=lambda: button_click(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",padx=25,pady=10,command=lambda: button_click(6))
b6.grid(row=2,column=2)

b7=Button(root,text="7",padx=25,pady=10,command=lambda: button_click(7))
b7.grid(row=3,column=0)
b8=Button(root,text="8",padx=25,pady=10,command=lambda: button_click(8))
b8.grid(row=3,column=1)
b9=Button(root,text="9",padx=25,pady=10,command=lambda: button_click(9))
b9.grid(row=3,column=2)

b10=Button(root,text="0",padx=25,pady=10 ,command=lambda:button_click(0))
b10.grid(row=4,column=0)
b11=Button(root,text="=",padx=25,pady=10,command=button_equal)
b11.grid(row=4,column=1)
b12=Button(root,text="+",padx=25,pady=10,command=button_add)
b12.grid(row=4,column=2)
b13=Button(root,text="-",padx=25,pady=10,command=button_subtract)
b13.grid(row=5,column=0)
b14=Button(root,text="*",padx=25,pady=10,command=button_multiply)
b14.grid(row=5,column=1 )
b15=Button(root,text="/",padx=25,pady=10,command=button_divide)
b15.grid(row=5,column=2)
b16=Button(root,text="clear",padx=70,pady=10,command=button_clear)
b16.grid(row=6,columnspan=3)
root.mainloop()