list_val = [20,47,40,79,20]

# list_val[1] = 100
list_val.insert(1,100)

list_val.append(200)

for value in list_val:
    print(value)

# Reverse a List Without Using reverse()

reverse_list = list_val[::-1]

print(reverse_list)

# Remove Duplicates from a List

Unique_value = []

for unique in list_val:
    if unique not in Unique_value:
        Unique_value.append(unique)

print(Unique_value)


# 4️⃣ Find the Second Largest Number in a List

first_larg = float('-inf') # negative infinity.
second_larg = float('-inf')

for num in Unique_value:
    if num > first_larg:
        second_larg = first_larg
        first_larg = num
    if first_larg > num > second_larg:
        second_larg = num


print(f"Second largest value: {second_larg}")


# 5️⃣ Flatten a Nested List
nested_list = [[1, 2, 3], [4, 5], [6]]

flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)


