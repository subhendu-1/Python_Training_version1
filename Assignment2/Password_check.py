# 8. Simple Password Strength Checker
# Input a password.
# If length < 6 → "Too short"
# If length between 6 and 10 → "Medium"
# If length > 10 → "Strong"


password = input("Enter your passwrod ")

password_len = len(password)

if password_len < 6:
    print("Too short")
elif password_len < 10:
    print("Medium")
else:
    print("Strong")