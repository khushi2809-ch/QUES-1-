#Hospital Emergency Triage
# Input from user
heart_rate_status = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Is there severe injury? (yes/no): ")
age = int(input("Enter patient age: "))
condition = input("Enter condition (critical/moderate/normal): ")

# Categorization
if heart_rate_status.lower() == "yes" or severe_injury.lower() == "yes":
    category = "Critical"

elif condition.lower() == "moderate":
    if age > 65:
        category = "Critical (Upgraded due to senior age)"
    else:
        category = "Moderate"

else:
    category = "Normal"

print("Patient Category:", category)
