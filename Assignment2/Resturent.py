Burger = 5
Pizza = 8
Coffee = 3

item = input("Enter Item name: ")
count = int(input("Enter Quantity of Items: "))

if item == "Burger":
    print(Burger * count)
elif item == "Pizza":
    print(Pizza * count)
    
else:
    print(Coffee * count)