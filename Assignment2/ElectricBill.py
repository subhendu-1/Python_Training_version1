unit = float(input("Enter the number of Units consumed: "))

initial_bill = 0.0

if unit <= 100:
    initial_bill = unit * 0.5
elif unit <= 300:
    initial_bill = (100 * 0.5) + ((unit - 100) * 0.75)
else:
    initial_bill = (100 * 0.5) + (200 * 0.75) + ((unit - 200) * 1.2)


print(f"Total Bill: ${initial_bill:.2f}" )
