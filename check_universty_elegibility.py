 #University Admission Eligibility
 # Input from user
percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance_score = float(input("Enter entrance exam score: "))

eligible = True   # Assume student is eligible

# Check conditions
if percentage < 75:
    print("Not Eligible: Minimum 75% required in 12th grade.")
    eligible = False

if maths.lower() != "yes":
    print("Not Eligible: Mathematics subject is mandatory.")
    eligible = False

if entrance_score < 80:
    print("Not Eligible: Entrance exam score must be at least 80.")
    eligible = False

# Final Result
if eligible:
    print("Congratulations! You are Eligible for Admission 🎉")
