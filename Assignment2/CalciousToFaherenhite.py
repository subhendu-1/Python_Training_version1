temparature_num = float(input("Enter the Temperature number: "))
temparature_unit = input("Enter the Temperature unit: ")

if temparature_unit == "Celsius" :
    temparature_num = (temparature_num * 9/5) + 32
    print(f"Celsius to Fahrenheit: {temparature_num} F")

else:
    temparature_num = (temparature_num - 32) * 5/9
    print(f"Faherenhite to Celsius: {temparature_num} C")

