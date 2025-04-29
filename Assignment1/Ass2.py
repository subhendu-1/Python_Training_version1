stock_A = 15
stock_B = 9
stock_C = '4' 
stock_D = False
rate_multiplier = 2.5
new_stock = None


if not stock_D:
    adjustment_value = (stock_A ** 2) // (int(stock_C) * stock_B) + int(rate_multiplier)

new_stock = stock_B + (adjustment_value % 7)

new_stock = new_stock - (stock_A & stock_B)

final_value = (((new_stock ^ stock_A) << 2) >> 1) & (stock_B | int(stock_C))
if final_value == 0:
    print("Empty Stock")
elif (final_value in [3, 5, 7, 9, 11]) or (final_value > rate_multiplier * stock_A - 10):
    print("Stock Alert")
else:
    print("Stock Normal")
    


