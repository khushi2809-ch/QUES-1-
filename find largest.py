#Find Largest in List
numbers = [10, 45, 23, 89, 12]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number =", largest)