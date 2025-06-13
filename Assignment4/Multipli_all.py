# 7️⃣ Multiply All Numbers

def multiply_all_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(f"Multiplication Result: {multiply_all_numbers(2, 3, 4)}")

