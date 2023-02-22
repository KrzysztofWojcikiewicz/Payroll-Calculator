# This is going to be a simple payroll calculator in accordance with Polish tax and social security laws.

from tkinter import *
from tkinter import ttk
from decimal import *

getcontext().prec = 2


def calculate():
    taxamount = float(vtaxbracket.get()) * (float(vgrossamount.get()) - (float(vgrossamount.get()) * float(vtaxexpenses.get())))
    netamount = float(vgrossamount.get()) - round(taxamount, 0)
    vtaxamount.set("{:.2f}".format(round(taxamount, 0)))
    vnetamount.set("{:.2f}".format(netamount))


root = Tk()
root.title("Payroll calculator")

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

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(frame, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(frame, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(frame, text="Taxes:", justify="left", width=35).grid(column=0, row=3)
ttk.Label(frame, text="Net pay:", justify="left", width=35).grid(column=0, row=4)

ttk.Entry(frame, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(frame, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(frame, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(frame, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(frame, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Label(frame, textvariable=vtaxamount, justify="right").grid(column=2, row=3)
ttk.Label(frame, textvariable=vnetamount, justify="right").grid(column=2, row=4)

ttk.Button(frame, text="Calculate", command=calculate).grid(column=4, row=0)


root.mainloop()
