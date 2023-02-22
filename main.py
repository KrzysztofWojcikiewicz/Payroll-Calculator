# This is going to be a simple payroll calculator in accordance with Polish tax and social security laws.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from decimal import *

getcontext().prec = 2


def calculate():

    try:
        taxamount = float(vtaxbracket.get()) * (float(vgrossamount.get()) - (float(vgrossamount.get()) * float(vtaxexpenses.get())))
        netamount = float(vgrossamount.get()) - round(taxamount, 0)
        vtaxamount.set("{:.2f}".format(round(taxamount, 0))+" PLN")
        vnetamount.set("{:.2f}".format(netamount)+" PLN")
    except ValueError:
        messagebox.showerror("Value error", "Error: You can only input numbers!\nUse full stop as a separator as such: 0.00")


def button1():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame4.grid_remove()
    bottom_frame1.grid(padx=20, pady=10, row=1)


def button2():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame4.grid_remove()
    bottom_frame2.grid(padx=20, pady=10, row=1)


def button3():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame4.grid_remove()
    bottom_frame3.grid(padx=20, pady=10, row=1)


def button4():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame4.grid_remove()
    bottom_frame4.grid(padx=20, pady=10, row=1)


root = Tk()
root.title("Payroll Calculator")


vgrossamount = StringVar()
vgrossamount.set("0")

vtaxbracket = StringVar()
vtaxbracket.set("0.12")

vtaxexpenses = StringVar()
vtaxexpenses.set("0.20")

vtaxamount = StringVar()
vtaxamount.set("0")

vnetamount = StringVar()
vnetamount.set("0")


top_frame = ttk.Frame(root)
top_frame.grid(pady=10, padx=20, row=0, sticky=W+E)

button1 = ttk.Button(top_frame, text="Contract for\nspecific work", command=button1, width=20)
button1.grid(row=0, column=0)
button2 = ttk.Button(top_frame, text="Contract of\nmandate", command=button2, width=20)
button2.grid(row=0, column=1)
button3 = ttk.Button(top_frame, text="Employment\n", command=button3, width=20)
button3.grid(row=0, column=2)
button4 = ttk.Button(top_frame, text="Self-employment\n", command=button4, width=20)
button4.grid(row=0, column=3)


bottom_frame1 = ttk.Frame(root)
bottom_frame1.grid(pady=10, padx=20, row=1)

ttk.Label(bottom_frame1, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame1, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame1, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame1, text="Taxes:", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame1, text="Net pay:", justify="left", width=35).grid(column=0, row=4)

ttk.Entry(bottom_frame1, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame1, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame1, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame1, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame1, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Label(bottom_frame1, textvariable=vtaxamount, justify="right").grid(column=2, row=3)
ttk.Label(bottom_frame1, textvariable=vnetamount, justify="right").grid(column=2, row=4)

ttk.Button(bottom_frame1, text="Calculate", command=calculate).grid(column=4, row=0)


bottom_frame2 = ttk.Frame(root)

ttk.Label(bottom_frame2, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame2, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame2, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame2, text="Taxes:", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame2, text="Net pay:", justify="left", width=35).grid(column=0, row=4)

ttk.Entry(bottom_frame2, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame2, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame2, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame2, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame2, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Label(bottom_frame2, textvariable=vtaxamount, justify="right").grid(column=2, row=3)
ttk.Label(bottom_frame2, textvariable=vnetamount, justify="right").grid(column=2, row=4)

ttk.Button(bottom_frame2, text="Calculate", command=calculate).grid(column=4, row=0)


bottom_frame3 = ttk.Frame(root)

ttk.Label(bottom_frame3, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame3, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame3, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame3, text="Taxes:", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame3, text="Net pay:", justify="left", width=35).grid(column=0, row=4)

ttk.Entry(bottom_frame3, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame3, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame3, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame3, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame3, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Label(bottom_frame3, textvariable=vtaxamount, justify="right").grid(column=2, row=3)
ttk.Label(bottom_frame3, textvariable=vnetamount, justify="right").grid(column=2, row=4)

ttk.Button(bottom_frame3, text="Calculate", command=calculate).grid(column=4, row=0)


bottom_frame4 = ttk.Frame(root)

ttk.Label(bottom_frame4, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame4, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame4, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame4, text="Taxes:", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame4, text="Net pay:", justify="left", width=35).grid(column=0, row=4)

ttk.Entry(bottom_frame4, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame4, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame4, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame4, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame4, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)


ttk.Label(bottom_frame4, textvariable=vtaxamount, justify="right").grid(column=2, row=3)
ttk.Label(bottom_frame4, textvariable=vnetamount, justify="right").grid(column=2, row=4)

ttk.Button(bottom_frame4, text="Calculate", command=calculate).grid(column=4, row=0)


root.mainloop()
