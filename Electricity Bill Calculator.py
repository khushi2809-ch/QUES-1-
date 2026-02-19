#Electricity Bill Calculator
# Input
units = float(input("Enter electricity units consumed: "))
age = int(input("Enter your age: "))

bill = 0

# Slab Calculation
if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# Senior Citizen Discount (age >= 60)
if age >= 60:
    discount = bill * 0.10
    bill = bill - discount
    print("Senior Citizen Discount Applied: ₹", discount)

print("Total Electricity Bill: ₹", bill)
