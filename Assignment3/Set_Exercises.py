# 1️⃣1️⃣ Remove Duplicates from a List Using a Set

list_value = [1, 2, 2, 3, 4, 4, 5] 

converted_set = set(list_value)

print(converted_set)


# 1️⃣2️⃣ Find Common Elements Between Two Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common_elements = set1.intersection(set2)
print("Common Elements:", common_elements)

# 1️⃣3️⃣ Perform Union and Difference on Two Sets

set3 = {1, 2, 3}
set4 = {2, 3, 4}

union_set = set3.union(set4)
difference_set = set3.difference(set4)

print("Union:", union_set)
print("Difference (set1 - set2):", difference_set)

# 1️⃣4️⃣ Check if a Set is a Subset of Another Set

set_a = {2, 3}
set_b = {1, 2, 3, 4, 5}

is_subset = set_a.issubset(set_b)

print("Is subset:", is_subset)


# 1️⃣5️⃣ Convert a Set to a List and Sort It

num_set = {5, 2, 8, 1, 4}


sorted_list = sorted(list(num_set))

print(sorted_list)


