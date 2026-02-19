#Income Tax Calculator (India Based)
# Input from user
income = float(input("Enter your annual income: "))
age = int(input("Enter your age: "))

tax = 0

# Set exemption limit
if age >= 60:
    exemption = 300000
else:
    exemption = 250000

# Tax Calculation
if income <= exemption:
    tax = 0

elif income <= 500000:
    tax = (income - exemption) * 0.05

elif income <= 1000000:
    tax = (500000 - exemption) * 0.05
    tax += (income - 500000) * 0.20

else:
    tax = (500000 - exemption) * 0.05
    tax += (1000000 - 500000) * 0.20
    tax += (income - 1000000) * 0.30

print("Total Tax Payable: ₹", tax)
