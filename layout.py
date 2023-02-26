# This is the main layout module for the application's GUI.

from tkinter import *
from tkinter import ttk
import calculator


def button1():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame1.grid(padx=20, pady=10, row=1)


def button2():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame2.grid(padx=20, pady=10, row=1)


def button3():
    bottom_frame1.grid_remove()
    bottom_frame2.grid_remove()
    bottom_frame3.grid_remove()
    bottom_frame3.grid(padx=20, pady=10, row=1)


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

vstud = IntVar()
vstud.set(1)

vage = IntVar()
vage.set(1)

vssec = IntVar()
vssec.set(0)

vsic = IntVar()
vsic.set(0)

vppk = IntVar()
vppk.set(0)

vpensionamount = StringVar()
vpensionamount.set("0")

vdisamount = StringVar()
vdisamount.set("0")

vsicamount = StringVar()
vsicamount.set("0")

vcapitalamount = StringVar()
vcapitalamount.set("0")

vhealthamount = StringVar()
vhealthamount.set("0")


top_frame = ttk.Frame(root)
top_frame.grid(pady=10, padx=20, row=0, sticky=W+E)

button1 = ttk.Button(top_frame, text="Contract for\nspecific work", command=button1, width=20)
button1.grid(row=0, column=0)
button2 = ttk.Button(top_frame, text="Contract of\nmandate", command=button2, width=20)
button2.grid(row=0, column=1)
button3 = ttk.Button(top_frame, text="Employment\n", command=button3, width=20)
button3.grid(row=0, column=2)

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

ttk.Button(bottom_frame1, text="Calculate", command=calculator.calculate_specific).grid(column=4, row=0)


bottom_frame2 = ttk.Frame(root)

ttk.Label(bottom_frame2, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame2, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame2, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame2, text="Student under the age of 26?", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame2, text="Person under the age of 26?", justify="left", width=35).grid(column=0, row=4)
ttk.Label(bottom_frame2, text="Obligatory/voluntary social insurance?", justify="left", width=35).grid(column=0, row=5)
ttk.Label(bottom_frame2, text="Voluntary sick allowance insurance?", justify="left", width=35).grid(column=0, row=6)
ttk.Label(bottom_frame2, text="Voluntary Employee Capital Plans?", justify="left", width=35).grid(column=0, row=7)

ttk.Label(bottom_frame2, text="Old age pension insurance:", justify="left", width=35).grid(column=0, row=8)
ttk.Label(bottom_frame2, text="Disability pension insurance:", justify="left", width=35).grid(column=0, row=9)
ttk.Label(bottom_frame2, text="Sickness allowance insurance:", justify="left", width=35).grid(column=0, row=10)
ttk.Label(bottom_frame2, text="Employee Capital Plans:", justify="left", width=35).grid(column=0, row=11)
ttk.Label(bottom_frame2, text="Health insurance:", justify="left", width=35).grid(column=0, row=12)
ttk.Label(bottom_frame2, text="Taxes:", justify="left", width=35).grid(column=0, row=13)
ttk.Label(bottom_frame2, text="Net pay:", justify="left", width=35).grid(column=0, row=14)

ttk.Entry(bottom_frame2, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame2, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame2, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame2, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame2, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Checkbutton(bottom_frame2, text="Yes", variable=vstud, onvalue=0, offvalue=1).grid(column=2, row=3)
ttk.Checkbutton(bottom_frame2, text="Yes", variable=vage, onvalue=0, offvalue=1).grid(column=2, row=4)
ttk.Checkbutton(bottom_frame2, text="Yes", variable=vssec).grid(column=2, row=5)
ttk.Checkbutton(bottom_frame2, text="Yes", variable=vsic).grid(column=2, row=6)
ttk.Checkbutton(bottom_frame2, text="Yes", variable=vppk).grid(column=2, row=7)

ttk.Label(bottom_frame2, textvariable=vpensionamount, justify="right").grid(column=2, row=8)
ttk.Label(bottom_frame2, textvariable=vdisamount, justify="right").grid(column=2, row=9)
ttk.Label(bottom_frame2, textvariable=vsicamount, justify="right").grid(column=2, row=10)
ttk.Label(bottom_frame2, textvariable=vcapitalamount, justify="right").grid(column=2, row=11)
ttk.Label(bottom_frame2, textvariable=vhealthamount, justify="right").grid(column=2, row=12)
ttk.Label(bottom_frame2, textvariable=vtaxamount, justify="right").grid(column=2, row=13)
ttk.Label(bottom_frame2, textvariable=vnetamount, justify="right").grid(column=2, row=14)

ttk.Button(bottom_frame2, text="Calculate", command=calculator.calculate_mandate).grid(column=4, row=0)


bottom_frame3 = ttk.Frame(root)

ttk.Label(bottom_frame3, text="Enter gross amount:", justify="left", width=35).grid(column=0, row=0)
ttk.Label(bottom_frame3, text="Pick your tax bracket:", justify="left", width=35).grid(column=0, row=1)
ttk.Label(bottom_frame3, text="Pick your tax deductible expenses:", justify="left", width=35).grid(column=0, row=2)
ttk.Label(bottom_frame3, text="Student under the age of 26?", justify="left", width=35).grid(column=0, row=3)
ttk.Label(bottom_frame3, text="Person under the age of 26?", justify="left", width=35).grid(column=0, row=4)
ttk.Label(bottom_frame3, text="Voluntary Employee Capital Plans?", justify="left", width=35).grid(column=0, row=7)

ttk.Label(bottom_frame3, text="Old age pension insurance:", justify="left", width=35).grid(column=0, row=8)
ttk.Label(bottom_frame3, text="Disability pension insurance:", justify="left", width=35).grid(column=0, row=9)
ttk.Label(bottom_frame3, text="Sickness allowance insurance:", justify="left", width=35).grid(column=0, row=10)
ttk.Label(bottom_frame3, text="Employee Capital Plans:", justify="left", width=35).grid(column=0, row=11)
ttk.Label(bottom_frame3, text="Health insurance:", justify="left", width=35).grid(column=0, row=12)
ttk.Label(bottom_frame3, text="Taxes:", justify="left", width=35).grid(column=0, row=13)
ttk.Label(bottom_frame3, text="Net pay:", justify="left", width=35).grid(column=0, row=14)

ttk.Entry(bottom_frame3, textvariable=vgrossamount, justify="right").grid(column=1, row=0, columnspan=2)

ttk.Radiobutton(bottom_frame3, text="12%", variable=vtaxbracket, value="0.12").grid(column=1, row=1)
ttk.Radiobutton(bottom_frame3, text="32%", variable=vtaxbracket, value="0.32").grid(column=2, row=1)

ttk.Radiobutton(bottom_frame3, text="20%", variable=vtaxexpenses, value="0.20").grid(column=1, row=2)
ttk.Radiobutton(bottom_frame3, text="50%", variable=vtaxexpenses, value="0.50").grid(column=2, row=2)

ttk.Checkbutton(bottom_frame3, text="Yes", variable=vstud, onvalue=0, offvalue=1).grid(column=2, row=3)
ttk.Checkbutton(bottom_frame3, text="Yes", variable=vage, onvalue=0, offvalue=1).grid(column=2, row=4)
ttk.Checkbutton(bottom_frame3, text="Yes", variable=vppk).grid(column=2, row=7)

ttk.Label(bottom_frame3, textvariable=vpensionamount, justify="right").grid(column=2, row=8)
ttk.Label(bottom_frame3, textvariable=vdisamount, justify="right").grid(column=2, row=9)
ttk.Label(bottom_frame3, textvariable=vsicamount, justify="right").grid(column=2, row=10)
ttk.Label(bottom_frame3, textvariable=vcapitalamount, justify="right").grid(column=2, row=11)
ttk.Label(bottom_frame3, textvariable=vhealthamount, justify="right").grid(column=2, row=12)
ttk.Label(bottom_frame3, textvariable=vtaxamount, justify="right").grid(column=2, row=13)
ttk.Label(bottom_frame3, textvariable=vnetamount, justify="right").grid(column=2, row=14)

ttk.Button(bottom_frame3, text="Calculate", command=calculator.calculate_employment).grid(column=4, row=0)
