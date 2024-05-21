from tkinter import *
import numpy as np
from math import sqrt
tki = Tk()

tki.title('Calculadora')
tki.geometry('300x200')
tki.configure(background = '#414352')
tki.resizable(False, False)

def clear():
	ent1.delete(0, END)
	ent2.delete(0,END)
	tx1.delete('1.0', END)

def quadr():
	try:
		resp = float(ent1.get())**2
	except ValueError:
		resp = 'Digite números!'

	tx1.delete('1.0', END)
	tx1.insert(END, resp)

def raiz():
	try:
		resp = sqrt(float(ent1.get()))
	except ValueError:
		resp = 'Digite números!'

	tx1.delete('1.0', END)
	tx1.insert(END, resp)

def soma():
	try:
		a = float(ent1.get())
		b = float(ent2.get())
		resp = a+b
	except ValueError:
		resp = 'Digite números!'

	tx1.delete('1.0', END)
	tx1.insert(END, resp)

def subt():
	try:
		a = float(ent1.get())
		b = float(ent2.get())
		resp = a - b
	except ValueError:
		resp = 'Digite números!'

	tx1.delete('1.0', END)
	tx1.insert(END, resp)

def  divis():
	try:
		a = float(ent1.get())
		b = float(ent2.get())
		try:
			resp = a/b
			resp = np.around(resp, 5)
		except ZeroDivisionError:
			resp = 'Não divisivel por 0'
	except ValueError:
		resp = 'Digite números!'
	tx1.delete('1.0', END)
	tx1.insert(END, resp)

def mult():
	try:
		a = float(ent1.get())
		b = float(ent2.get())
		resp = a * b
		resp = np.around(resp, 5)
	except ValueError:
		resp = 'Digite números!'

	tx1.delete('1.0', END)
	tx1.insert(END, resp)

lb1 = Label(tki, text = 'Insira o 1° número: ', bg = '#414352')
lb2 = Label(tki, text = 'Insira o 2° número: ', bg = '#414352')
e1 = StringVar()
e2 = StringVar()
ent1 = Entry(tki, width=12, textvariable = e1)
ent2 = Entry(tki, width=12, textvariable = e2)

bt1 = Button(tki, text = 'Soma', command = soma, width=8, bd=3, relief='ridge')
bt2 = Button(tki, text='Subtrair', command=subt, width=8, bd=3, relief='ridge')
bt3 = Button(tki, text='Dividir', command=divis, width=8, bd=3, relief='ridge')
bt4 = Button(tki, text='Multiplicar', command=mult, width=8, bd=3, relief='ridge')
bt5 = Button(tki, text='Limpar', command=clear, width=8, bd=3, relief='ridge')
bt6 = Button(tki, text='1°número²', command=quadr, width=8, bd=3, relief='ridge')
bt7 = Button(tki, text='√1°número', command=raiz, width=8, bd=3, relief='ridge')

tx1 = Text(tki, height = 1, width = 20 )
def desabilitar_modificacao(event):
	return "break"
tx1.bind('<Key>', desabilitar_modificacao)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0, pady=5)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
bt1.grid(row=2, column=0)
bt2.grid(row=3, column=0, pady=4)
bt3.grid(row=4, column=0)
bt4.grid(row=5, column=0, pady=4)
bt5.grid(row=3, column=1)
bt6.grid(row=4, column=1)
bt7.grid(row=5, column=1)
tx1.grid(row=2,column=1, padx=5, pady=4)


tki.mainloop()