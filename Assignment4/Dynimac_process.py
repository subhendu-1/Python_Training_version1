def order_summary(name, *items, discount=0, **prices):
    print(f"Order for {name}:")
    print(f"Items: {', '.join(items)}")
    print(f"Prices: {prices}")
    
    total_cost = sum(prices[item] for item in items)
    print(f"Total Cost before discount: ${total_cost}")
    
    discount_amount = (discount / 100) * total_cost
    final_total = total_cost - discount_amount
    print(f"Discount Applied: {discount}%")
    print(f"Final Total: ${final_total}")


order_summary("John", "Pizza", "Burger", "Fries", discount=10, Pizza=12, Burger=8, Fries=5)
