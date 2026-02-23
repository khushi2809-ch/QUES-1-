# Inventory Management System

# Step 1: Input product stock quantities
stocks = []
n = int(input("Enter number of products: "))

for i in range(n):
    qty = int(input(f"Enter stock quantity of product {i+1}: "))
    stocks.append(qty)

print("\nOriginal Stock List:", stocks)

# Step 2: Remove items with 0 stock
updated_stocks = []

for qty in stocks:
    if qty != 0:
        updated_stocks.append(qty)

print("After Removing 0 Stock Items:", updated_stocks)

# Step 3: Add restock (50 units) to items below 10
for i in range(len(updated_stocks)):
    if updated_stocks[i] < 10:
        updated_stocks[i] += 50

print("After Restocking Low Items:", updated_stocks)

# Step 4: Find total inventory count
total_inventory = sum(updated_stocks)

print("Total Inventory Count:", total_inventory)

'''output example:
Enter number of products: 5
Enter stock quantity of product 1: 0
Enter stock quantity of product 2: 5
Enter stock quantity of product 3: 15
Enter stock quantity of product 4: 8
Enter stock quantity of product 5: 0
Original Stock List: [0, 5, 15, 8, 0]
After Removing 0 Stock Items: [5, 15, 8]
After Restocking Low Items: [55, 15, 58]
Total Inventory Count: 128
'''
