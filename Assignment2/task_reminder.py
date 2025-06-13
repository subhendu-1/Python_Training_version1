# 10. Daily Task Reminder
# Ask user what day it is:
# Monday to Friday → "Work day"
# Saturday → "Family time"
# Sunday → "Relax day"


user_day = input("Enter your preferece day: ")

if user_day == "Saturday":
    print("Family time")

elif user_day == "Sunday":
    print("Relax day")

else:
    print("Work Day")