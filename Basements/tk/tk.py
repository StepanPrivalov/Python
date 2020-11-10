import tkinter as tk
from tkinter import messagebox as mb
import random as r
''' # calculator(mini)
def mul():
	a = str(int(en1.get()) * int(en2.get()))
	lb.config(fg = "#000000", text = a)

scr = tk.Tk()
scr.geometry("300x150+300+300")

en1 = tk.Entry(scr)
en2 = tk.Entry(scr)
lb = tk.Label(scr)

bt = tk.Button(scr, text = "Вычислить", command = mul, border = 5)

en1.pack()
en2.pack()
bt.pack()
lb.pack()

scr.mainloop()
'''
global leftB, rightB, currentNum, res, i
res, currentNum = 0, 1
i = 0
leftB = -100 * currentNum
rightB = 100 * currentNum


def startSearch():
	global res, leftB, rightB, currentNum, i
	if en1.get() != "":
		try:
			currentNum = int(en1.get())
			leftB = -10 * currentNum
			rightB = 10 * currentNum
			res = r.randint(leftB, rightB)
			lb.config(fg = "black", text = str(res))
			i += 1
			lb4.config(fg = "black", text = str(i))
		except ValueError:
			mb.showerror(title = "Error", message = "Not num u moron!")
	else:
		mb.showerror(title = "Error", message = "Enter number!")


def More():
	global res, leftB, rightB, currentNum, i
	leftB = res
	res = r.randint(leftB, rightB)
	lb.config(fg = "black", text = str(res))
	i += 1
	lb4.config(fg = "black", text = str(i))

def Less():
	global res, leftB, rightB, currentNum, i
	rightB = res
	res = r.randint(leftB, rightB)
	lb.config(fg = "black", text = str(res))
	i += 1
	lb4.config(fg = "black", text = str(i))

def Clear():
	global i
	i = 0
	en1.delete(0, "end")
	lb4.config(fg = "black", text = "")
	lb.config(fg = "black", text = "")

def Right():
	global res
	mb.showinfo(title = "Victory!!!", message = "That's right! The num is - " + str(res))

ass = tk.Tk()
rows = 0


en1 = tk.Entry(ass)
lb = tk.Label(ass)
lb1 = tk.Label(ass)
lb2 = tk.Label(ass)
lb3 = tk.Label(ass)
lb4 = tk.Label(ass)
b = tk.Button(ass, text = "Start searching", border = 5, command = startSearch)
but1 = tk.Button(ass, text = "   More  ", border = 5, command = More)
but2 = tk.Button(ass, text = "   Less  ", border = 5, command = Less)
but3 = tk.Button(ass, text = "  Right  ", border = 5, command = Right)
but4 = tk.Button(ass, text = "About Programm", border = 5, command = lambda: mb.showinfo(title = "Info", message = "This algorithm ...."))
but5 = tk.Button(ass, text = "  Clear  ", border = 5,command = Clear)

lb1.config(text = "  Enter num to search: ")
lb2.config(text = "  That's what i found:  ")
lb3.config(text = "Amount of tries:  ")


en1.grid(column = 2, columnspan = 2, row = 1 )
lb1.grid(column = 0, columnspan = 2, row = 1)
b.grid(columnspan = 5, row = 2)
lb2.grid(column = 0,columnspan = 2, row = 3)
lb.grid(column = 2, columnspan = 2, row = 3 )
but1.grid(column = 0, row = 4)
but2.grid(column = 1, columnspan = 2, row = 4)
but3.grid(column = 3, row = 4)
lb3.grid(row = 5, column = 0,)
lb4.grid(row = 5, column = 3, columnspan = 2)
but4.grid(row = 6, column = 0, columnspan = 3)
but5.grid(row = 6, column = 3, columnspan = 2)


ass.mainloop() 