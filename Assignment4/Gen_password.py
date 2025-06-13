# 3️⃣ Generate a Password (Random 6-Digit)

import random

def generate_password():
    password = random.randint(100000, 999999)
    return password


print(f"Generated Password: {generate_password()}")


