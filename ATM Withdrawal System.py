#ATM Withdrawal System
# Input
balance = float(input("Enter your account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

# Conditions Check
if withdraw_amount > balance:
    print("Transaction Failed ❌: Insufficient Account Balance.")

elif withdraw_amount > 50000:
    print("Transaction Failed ❌: Daily withdrawal limit is ₹50,000.")

elif withdraw_amount > atm_cash:
    print("Transaction Failed ❌: ATM does not have sufficient cash.")

else:
    balance -= withdraw_amount
    print("Transaction Successful ✅")
    print("Remaining Balance: ₹", balance)
