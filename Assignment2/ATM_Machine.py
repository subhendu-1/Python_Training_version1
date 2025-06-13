initial_balance = 5000

while True:
    operation = input("What Operation you want to perform: ")
    if operation == "Withdraw":
        debite_amount = float(input("Enter how much amout you want to withdraw: "))
        if debite_amount < initial_balance:
            initial_balance = initial_balance - debite_amount
            print(f"{debite_amount} Debited Successfuly")
        else:
            print("Insufficient Balance")
    elif operation == "Check Balance":
        print(f"Current balance in your account is : {initial_balance}")
    