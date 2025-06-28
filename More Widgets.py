from tkinter import *
from datetime import date
root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')
lbl = Label(text = 'Hey there!', fg = 'white', bg = '#30fc03', height = '1', width = 300)
namelbl = Label(text="Full Name", bg='#03a5fc')
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is:"
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#fc7703", fg="white")
lbl.pack()
namelbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()