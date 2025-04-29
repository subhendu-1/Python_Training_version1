speed = int(input("Enter the speed: "))

if speed <= 60:
    print("no fine")
elif speed <= 80:
    print("$100 fine")
elif  speed <= 100:
    print("$300 fine")
else:
    print("Lisence Required")