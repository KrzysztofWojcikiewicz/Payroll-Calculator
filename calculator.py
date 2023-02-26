# This is main calculating module for the application.

from tkinter import messagebox
import decimal
import layout

decimal.getcontext().prec = 4


def calculate_specific():

    try:
        taxamount = float(layout.vtaxbracket.get()) * (float(layout.vgrossamount.get()) - (float(layout.vgrossamount.get()) * float(layout.vtaxexpenses.get())))
        netamount = float(layout.vgrossamount.get()) - round(taxamount, 0)
        layout.vtaxamount.set("{:.2f}".format(round(taxamount, 0))+" PLN")
        layout.vnetamount.set("{:.2f}".format(netamount)+" PLN")
    except ValueError:
        messagebox.showerror("Value error", "Error: You can only input numbers!\nUse full stop as a separator as such: 0.00")


def calculate_mandate():

    try:
        pensionamount = round(round(float(layout.vgrossamount.get()), 2) * 0.0976 * layout.vssec.get(), 2)
        disamount = float(layout.vgrossamount.get()) * 0.015 * layout.vssec.get()
        sicamount = float(layout.vgrossamount.get()) * 0.0245 * layout.vsic.get()
        capitalamount = float(layout.vgrossamount.get()) * 0.02 * layout.vppk.get() * layout.vssec.get()
        capitaltax = float(layout.vgrossamount.get()) * 0.015 * layout.vppk.get() * layout.vssec.get()
        healthamount = round(round((float(layout.vgrossamount.get()) - (pensionamount + disamount + sicamount)), 2) * 0.09 * layout.vstud.get(), 2)
        taxexpenence = ((float(layout.vgrossamount.get()) + float(capitaltax)) - (pensionamount + disamount + sicamount)) * float(layout.vtaxexpenses.get())
        taxbaseamount = round((float(layout.vgrossamount.get()) + capitaltax) - (pensionamount + disamount + sicamount + taxexpenence), 0)

        taxamount = taxbaseamount * float(layout.vtaxbracket.get()) * layout.vage.get() * layout.vstud.get()
        netamount = float(layout.vgrossamount.get()) - (round(taxamount, 0) + round(pensionamount, 2) + round(disamount, 2) + round(sicamount, 2) + round(capitalamount, 2) + round(healthamount, 2))

        layout.vpensionamount.set("{:.2f}".format(round(pensionamount, 2)) + " PLN")
        layout.vdisamount.set("{:.2f}".format(round(disamount, 2)) + " PLN")
        layout.vsicamount.set("{:.2f}".format(round(sicamount, 2)) + " PLN")
        layout.vcapitalamount.set("{:.2f}".format(round(capitalamount, 2)) + " PLN")
        layout.vhealthamount.set("{:.2f}".format(round(healthamount, 2))+" PLN")
        layout.vtaxamount.set("{:.2f}".format(round(taxamount, 0))+" PLN")
        layout.vnetamount.set("{:.2f}".format(netamount)+" PLN")
    except ValueError:
        messagebox.showerror("Value error", "Error: You can only input numbers!\nUse full stop as a separator as such: 0.00")


def calculate_employment():

    try:
        pensionamount = round(round(float(layout.vgrossamount.get()), 2) * 0.0976, 2)
        disamount = float(layout.vgrossamount.get()) * 0.015
        sicamount = float(layout.vgrossamount.get()) * 0.0245
        capitalamount = float(layout.vgrossamount.get()) * 0.02 * layout.vppk.get()
        capitaltax = float(layout.vgrossamount.get()) * 0.015 * layout.vppk.get()
        healthamount = round(round((float(layout.vgrossamount.get()) - (pensionamount + disamount + sicamount)), 2) * 0.09 * layout.vstud.get(), 2)
        taxexpenence = ((float(layout.vgrossamount.get()) + float(capitaltax)) - (pensionamount + disamount + sicamount)) * float(layout.vtaxexpenses.get())
        taxbaseamount = round((float(layout.vgrossamount.get()) + capitaltax) - (pensionamount + disamount + sicamount + taxexpenence), 0)

        taxamount = taxbaseamount * float(layout.vtaxbracket.get()) * layout.vage.get() * layout.vstud.get()
        netamount = float(layout.vgrossamount.get()) - (round(taxamount, 0) + round(pensionamount, 2) + round(disamount, 2) + round(sicamount, 2) + round(capitalamount, 2) + round(healthamount, 2))

        layout.vpensionamount.set("{:.2f}".format(round(pensionamount, 2)) + " PLN")
        layout.vdisamount.set("{:.2f}".format(round(disamount, 2)) + " PLN")
        layout.vsicamount.set("{:.2f}".format(round(sicamount, 2)) + " PLN")
        layout.vcapitalamount.set("{:.2f}".format(round(capitalamount, 2)) + " PLN")
        layout.vhealthamount.set("{:.2f}".format(round(healthamount, 2))+" PLN")
        layout.vtaxamount.set("{:.2f}".format(round(taxamount, 0))+" PLN")
        layout.vnetamount.set("{:.2f}".format(netamount)+" PLN")
    except ValueError:
        messagebox.showerror("Value error", "Error: You can only input numbers!\nUse full stop as a separator as such: 0.00")