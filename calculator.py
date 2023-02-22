# This is main calculating module for the application.

from tkinter import messagebox
import layout


def calculate():

    try:
        taxamount = float(layout.vtaxbracket.get()) * (float(layout.vgrossamount.get()) - (float(layout.vgrossamount.get()) * float(layout.vtaxexpenses.get())))
        netamount = float(layout.vgrossamount.get()) - round(taxamount, 0)
        layout.vtaxamount.set("{:.2f}".format(round(taxamount, 0))+" PLN")
        layout.vnetamount.set("{:.2f}".format(netamount)+" PLN")
    except ValueError:
        messagebox.showerror("Value error", "Error: You can only input numbers!\nUse full stop as a separator as such: 0.00")
