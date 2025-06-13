# 8️⃣ Generate an Invoice (Use kwargs)

def generate_invoice(**items):
    total = 0
    for item, price in items.items():
        print(f"{item}: ${price}")
        total += price
    print(f"Total: ${total}")


generate_invoice(Shirt=20, Jeans=40, Shoes=60)
