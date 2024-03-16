from tkinter import *
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
but1=Label(window, text='Hello, world!')
but1.grid(column=0, row=0)
but2=Label(window, text='')
but2.grid(column=1, row=0)
but3=Label(window, text='')
but3.grid(column=0, row=1)

e=Entry(window, width=50, bg='blue', fg='white', borderwidth=5)
e.grid(column=2, row=0)
e.insert(0, 'iohwfie')

def clc():
    hello=e.get()
    but4 = Label(window, text='My name is '+hello)
    but4.grid(column=2, row=2)

clkbut=Button(window, text='press me',command=clc,  fg='blue', bg='white')
clkbut.grid(column=4, row=0)
window.mainloop()



