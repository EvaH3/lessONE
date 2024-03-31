from tkinter import *
window = Tk()
window.title("Калькулятор для гуманитариев")

f_num=0.
command=''

e=Entry(window, width=25, bg='white', fg='black', borderwidth=3)
e.grid(column=0, row=0)
e.insert(0, f_num)

def clc1():
    global command
    command+='1'
    e.delete(0, END)
    e.insert(0, command)
def clc2():
    global command
    command+='2'
    e.delete(0, END)
    e.insert(0, command)
def clc3():
    global command
    command+='3'
    e.delete(0, END)
    e.insert(0, command)
def clc4():
    global command
    command+='4'
    e.delete(0, END)
    e.insert(0, command)
def clc5():
    global command
    command+='5'
    e.delete(0, END)
    e.insert(0, command)
def clc6():
    global command
    command+='6'
    e.delete(0, END)
    e.insert(0, command)
def clc7():
    global command
    command+='7'
    e.delete(0, END)
    e.insert(0, command)
def clc8():
    global command
    command+='8'
    e.delete(0, END)
    e.insert(0, command)
def clc9():
    global command
    command+='9'
    e.delete(0, END)
    e.insert(0, command)
def clc0():
    global command
    command += '0'
    e.delete(0, END)
    e.insert(0, command)
def clc0():
    global command
    command+='0'
    e.delete(0, END)
    e.insert(0, command)
def clcplus():
    global command
    command+='+'
    e.delete(0, END)
    e.insert(0, command)
def clcmin():
    global command
    command+='-'
    e.delete(0, END)
    e.insert(0, command)
def clcdel():
    global command
    command+='/'
    e.delete(0, END)
    e.insert(0, command)
def clcumn():
    global command
    command+='*'
    e.delete(0, END)
    e.insert(0, command)
def clcclr():
    global command
    e.delete(0, END)
    e.insert(0, '0')
    command=''
def clcres():
    global command, f_num
    f_num=round(eval(command),3)
    command=str(f_num)
    e.delete(0, END)
    e.insert(0, f_num)

but1=Button(window, text=' 1 ',command=clc1,  fg='blue', bg='white', height=3, width=5)
but2=Button(window, text=' 2 ',command=clc2,  fg='blue', bg='white', height=3, width=5)
but3=Button(window, text=' 3 ',command=clc3,  fg='blue', bg='white', height=3, width=5)

but4=Button(window, text=' 4 ',command=clc4,  fg='blue', bg='white', height=3, width=5)
but5=Button(window, text=' 5 ',command=clc5,  fg='blue', bg='white', height=3, width=5)
but6=Button(window, text=' 6 ',command=clc6,  fg='blue', bg='white', height=3, width=5)

but7=Button(window, text=' 7 ',command=clc7,  fg='blue', bg='white', height=3, width=5)
but8=Button(window, text=' 8 ',command=clc8,  fg='blue', bg='white', height=3, width=5)
but9=Button(window, text=' 9 ',command=clc9,  fg='blue', bg='white', height=3, width=5)

but0=Button(window, text=' 0 ',command=clc0,  fg='blue', bg='white', height=3, width=5)
butplus=Button(window, text=' + ',command=clcplus,  fg='blue', bg='white', height=3, width=5)
butmin=Button(window, text=' - ',command=clcmin,  fg='blue', bg='white', height=3, width=5)

butumn=Button(window, text=' * ',command=clcumn,  fg='blue', bg='white', height=3, width=5)
butdel=Button(window, text=' / ',command=clcdel,  fg='blue', bg='white', height=3, width=5)
butres=Button(window, text=' = ',command=clcres,  fg='blue', bg='white', height=3, width=5)

butclr=Button(window, text=' clear ',command=clcclr,  fg='blue', bg='white', width=10)

mass=[but7, but8,but9,but4,but5,but6,but3,but2,but1,but0,butplus,butmin,butumn,butdel,butres]

t=0
for i in range(2, 7):
    for j in range(2, 5):
        mass[t].grid(column=j, row=i)
        t+=1
butclr.grid(column=0, row=3)

window.mainloop()