# This is going to be a simple payroll calculator in accordance with Polish tax and social security laws.

print("Greetings!\nThis is a payroll calculator for different forms of employment in Poland.\nThis version handles contract for a specific work only.\n")

gross_amonut = float(input("Please enter the gross amount: "))
tax_bracket = (input("Are you in a lower tax bracket (income less than 120k in a year)? (Y/N)?: ")).lower()
tax_rate = 0

if tax_bracket == "y":
    tax_rate = 0.12
elif tax_bracket == "n":
    tax_rate = 0.32
else:
    print("Wrong value entered. Terminating.")
    exit()


tax_deduct = (input("Are you eligible for an increased tax deductible expenses? (Y/N)?: ")).lower()

if tax_deduct == "y":
    tax_deduct_rate = 0.5
elif tax_deduct == "n":
    tax_deduct_rate = 0.2
else:
    print("Wrong value entered. Terminating.")
    exit()

taxes = round((gross_amonut - (gross_amonut*tax_deduct_rate)) * tax_rate, 0)

nett_amount = gross_amonut - taxes


print(f"Your nett pay amount is: {int(nett_amount)},00 PLN\nAnd the amount of taxes is: {int(taxes)},00 PLN")
exit()
