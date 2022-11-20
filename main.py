from tkinter import*
import sqlite3

window=Tk()
window.title
window.geometry('200x120')
window.config(bg='#3b3b3b')
inputAction = ''
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE products (name TEXT, price TEXT, number TEXT)')
#connection.commit()
res = cur.fetchall()
def catalog(action):
    global inputAction
    global n0
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global nall
    global n0
    if action == '1' or action == '2' or action == '3' or action == '4':
        inputAction = action
        if inputAction == '1':
            n0 = input('Enter name')
            n1 = input(input('Enter price'))
            n2 = input(input('Enter number'))
            cur.execute(f'INSERT INTO products (name, price, number) VALUES ("{n0}", "{n1}", "{n2}")')
            connection.commit()
        if inputAction == '2':
            n0 = input('Enter row id')
            n1 = input(input('Enter'))
            n2 = input(input('Enter'))

button = Button(text='4', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:catalog('1'))
button.grid(row=2, column=1)
button = Button(text='4', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:catalog('2'))
button.grid(row=2, column=2)
button = Button(text='4', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:catalog('3'))
button.grid(row=1, column=1)
button = Button(text='4', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:catalog('4'))
button.grid(row=1, column=2)
cur.execute('SELECT rewid, name, price, number FROM productss')
connection.commit()
res = cur.fetchall()

label = Label(text_=res, font='Arial 20', fg='Black', bg='#3b3b3b')
label.grid(columnspan_=_3)
window.mainloop()