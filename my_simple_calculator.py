from tkinter import Tk, Button, Entry, END

root = Tk()
root.title("My Simple Calculator")

# Entry Field:

entry = Entry(root, width=20, borderwidth=5)
entry.grid(row=0,column=0,columnspan=3, padx=10, pady=10 )

# Functions:

def multiply():
    number = entry.get()
    global num
    global math
    math = "*"
    num = float(number)
    entry.delete(0,END)

def divide():
    number = entry.get()
    global num
    global math
    math = "/"
    num = float(number)
    entry.delete(0, END)
    
def add():
    number = entry.get()
    global num
    global math
    math = "+"
    num = float(number)
    entry.delete(0,END)

def substrat():
    number = entry.get()
    global num
    global math
    math = "-"
    num = float(number)
    entry.delete(0,END)
    

def click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(number))
    
def equal():
    number = entry.get()    
    entry.delete(0,END)
    if number!="0":
        if math == "+":
            entry.insert(0, num + int(number))
        elif math == "-":
            entry.insert(0, num - int(number))
        elif math == "*":
            entry.insert(0, num * int(number))
        elif math == "/":
            entry.insert(0, num / int(number))
        else:
            pass

def clear():
    entry.delete(0,END)


# Defining Buttons:

button_0 = Button(root,text="0", padx=40, pady=20, command=lambda: click(0))
button_1 = Button(root,text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root,text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root,text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root,text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root,text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root,text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root,text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root,text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root,text="9", padx=40, pady=20, command=lambda: click(9))
button_equal = Button(root,text="=", padx=40, pady=20, command=equal)
button_clear = Button(root,text="clear", padx=40, pady=20, command=clear)
button_divide = Button(root,text="/", padx=40, pady=20, command=divide)
button_multiply = Button(root,text="*", padx=40, pady=20, command=multiply)
button_add = Button(root,text="+", padx=40, pady=20, command=add)
button_substract = Button(root,text="-", padx=40, pady=20, command=substrat)



# Buttons Grids:

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=5,column=1)
button_equal.grid(row=4,column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_add.grid(row=5,column=2)
button_divide.grid(row=4,column=1)

root.mainloop()
 
