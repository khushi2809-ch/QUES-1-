# E-Commerce Cart System

# Step 1: Input product prices
prices = []
n = int(input("Enter number of products: "))

for i in range(n):
    price = float(input(f"Enter price of product {i+1}: ₹"))
    prices.append(price)

# Step 2: Remove duplicate items
unique_prices = list(set(prices))

# Step 3: Calculate total
total = sum(unique_prices)

print("\nPrices after removing duplicates:", unique_prices)
print("Total amount before discount: ₹", total)

# Step 4: Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
    total = total - discount
    print("Discount applied (10%): ₹", discount)
else:
    print("No discount applied.")

# Step 5: Add 18% GST
gst = total * 0.18
final_amount = total + gst

# Step 6: Display final payable amount
print("GST (18%): ₹", gst)
print("Final Payable Amount: ₹", final_amount)

'''output example:
Enter number of products: 5
Enter price of product 1: ₹1000
Enter price of product 2: ₹2000
Enter price of product 3: ₹3000
Enter price of product 4: ₹2000
Enter price of product 5: ₹4000
Prices after removing duplicates: [1000.0, 2000.0, 3000.0, 4000.0]
Total amount before discount: ₹ 10000.0
Discount applied (10%): ₹ 1000.0
GST (18%): ₹ 1620.0
Final Payable Amount: ₹ 10620.0
'''
