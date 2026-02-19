#Banking – Suspicious Transaction Detection
# Input from user
amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age in months: "))
international = input("Is the transaction international? (yes/no): ")

# Check conditions
if amount > 200000 and account_age < 6 and international.lower() == "yes":
    print("Transaction Flagged for Manual Verification 🚩")
else:
    print("Transaction is Normal ✅")
