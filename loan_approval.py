 #Loan Approval System
# Input from user
credit_score = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))

# Loan Decision
if credit_score < 600:
    print("Loan Rejected ❌ (Credit score below 600)")

elif 600 <= credit_score < 750:
    # Further income & loan check
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected ❌ (Low income and high existing loan)")
    else:
        print("Loan Approved ✅ (After income verification)")

else:  # credit_score >= 750
    print("Loan Approved ✅ (High credit score)")
