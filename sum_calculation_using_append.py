# Empty list banayi
numbers = []

# User se 5 numbers lena
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)   # Number list me add ho raha hai

# Sum calculate karna
total = sum(numbers)

print("Numbers =", numbers)
print("Total Sum =", total)
# append() → har input ko list ke end me add karta hai

# sum(numbers) → list ke sabhi elements ka total nikalta hai