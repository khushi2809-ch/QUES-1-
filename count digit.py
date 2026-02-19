#Count Digits in a Number
num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Total digits =", count)