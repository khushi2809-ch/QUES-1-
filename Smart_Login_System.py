#Smart Login System
# Predefined correct credentials
correct_username = "khushi"
correct_password = "12345"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful ✅")
        break
    else:
        attempts += 1
        print("Invalid Username or Password ❌")
        print("Attempts left:", max_attempts - attempts)

# Account lock condition
if attempts == max_attempts:
    print("Account Locked 🔒 (Maximum attempts reached)")
