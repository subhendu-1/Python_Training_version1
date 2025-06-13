# 9. Taxi Fare Calculator
# User inputs kilometers traveled.
# Up to 5 km → $10
# 6 to 15 km → $20
# 16 to 25 km → $30
# Above 25 km → $50
# Print the fare.


traveled = int(input("Enter How much Kilometers traveled: "))

if traveled <= 5:
    print(f"The fare price of your {traveled} km travle is {10}")

elif traveled <= 15:
    print(f"The fare price of your {traveled} km travle is {20}")

elif traveled <= 25:
    print(f"The fare price of your {traveled} km travle is {30}")

else:
    print(f"The fare price of your {traveled} km travle is {50}")