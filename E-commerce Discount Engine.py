#E-commerce Discount Engine
# Input from user
cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

# Discount variables
discount_cart = 0
discount_membership = 0
discount_festival = 0

# Cart Value Discount
if cart_value >= 10000:
    discount_cart = 15
elif cart_value >= 5000:
    discount_cart = 10
elif cart_value >= 2000:
    discount_cart = 5

# Membership Discount
if membership.lower() == "silver":
    discount_membership = 5
elif membership.lower() == "gold":
    discount_membership = 10
elif membership.lower() == "platinum":
    discount_membership = 20

# Festival Discount
if festival.lower() == "yes":
    discount_festival = 10

# Find Highest Discount
max_discount = max(discount_cart, discount_membership, discount_festival)

# Calculate Final Amount
final_amount = cart_value - (cart_value * max_discount / 100)

print("Highest Discount Applied:", max_discount, "%")
print("Final Payable Amount: ₹", final_amount)
