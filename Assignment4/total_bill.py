def calculate_total_bill(price, tax_rate):
    tax = price * (tax_rate / 100)
    total = price + tax
    return total

price = 129
tax_rate = 5  
print(f"Total price including tax: {calculate_total_bill(price, tax_rate)}")
