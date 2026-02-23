# Bank Transaction Analyzer

# Step 1: Input transactions
transactions = []
n = int(input("Enter number of transactions: "))

for i in range(n):
    amount = float(input(f"Enter transaction {i+1} (Deposit + / Withdrawal -): ₹"))
    transactions.append(amount)

print("\nAll Transactions:", transactions)

# Step 2: Calculate total balance
total_balance = sum(transactions)
print("Total Balance: ₹", total_balance)

# Step 3: Find largest withdrawal
withdrawals = []

for t in transactions:
    if t < 0:
        withdrawals.append(t)

if len(withdrawals) > 0:
    largest_withdrawal = min(withdrawals)   # Most negative value
    print("Largest Withdrawal: ₹", largest_withdrawal)
else:
    print("No withdrawals found.")

# Step 4: Count deposits greater than ₹10,000
count_deposits = 0

for t in transactions:
    if t > 10000:
        count_deposits += 1

print("Number of Deposits greater than ₹10,000:", count_deposits)

''' output example:
Enter number of transactions: 5
Enter transaction 1 (Deposit + / Withdrawal -): ₹5000
Enter transaction 2 (Deposit + / Withdrawal -): ₹-2000
Enter transaction 3 (Deposit + / Withdrawal -): ₹15000
Enter transaction 4 (Deposit + / Withdrawal -): ₹-500
Enter transaction 5 (Deposit + / Withdrawal -): ₹8000
All Transactions: [5000.0, -2000.0, 15000.
0, -500.0, 8000.0]
Total Balance: ₹ 26000.0
Largest Withdrawal: ₹ -2000.0
Number of Deposits greater than ₹10,000: 1
'''
