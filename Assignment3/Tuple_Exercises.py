# 6️⃣ Convert a List to a Tuple and Access Elements

list_val = [23,29,39,44,50]

tuple_val = tuple(list_val)

print(tuple_val)

first_val = tuple_val[0]
last_val = tuple_val[-1]
print(tuple_val,first_val,last_val,sep = ",")


# 7️⃣ Find the Index of an Element in a Tuple
# 📌 Task: Find the index of 50 in (10, 20, 30, 40, 50, 60).
# ✅ Expected Output: 4
find_val = 50

for index in range(len(tuple_val)):
    if  tuple_val[index] == find_val:
        print(index)


# 8️⃣ Merge Two Tuples

first_tuple = (1,2,3)
second_tuple = (4,5,6)

marge_tuple = first_tuple + second_tuple

print(marge_tuple)


# 9️⃣ Count Occurrences of an Element in a Tuple

repeted_tuple = (1, 2, 2, 3, 4, 2, 5)

clean_tuple = set(repeted_tuple)
len_repeted = len(repeted_tuple)
len_clean = len(clean_tuple)

count = len_repeted - len_clean


print(f"The number of 2 is {count+1}")


# 🔟 Find the Maximum and Minimum in a Tuple

tuple_value = (5, 10, 20, 1, 25)

max_value = max(tuple_value)
min_value = min(tuple_value)

print(max_value)
print(min_value)




