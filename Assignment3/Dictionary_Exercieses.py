# 1️⃣6️⃣ Create a Dictionary and Access Values

student_first = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

print(student_first['city'])

# 1️⃣7️⃣ Update a Dictionary

student_second = {'name': 'Alice', 'age': 25}


student_second['city'] = 'NYC'

print(student_second)

# 1️⃣8️⃣ Merge Two Dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)

# 1️⃣9️⃣ Iterate Through a Dictionary and Print Key-Value Pairs

my_dict = {'x': 10, 'y': 20, 'z': 30}

for key, value in my_dict.items():
    print(f"{key} : {value}")

# 2️⃣0️⃣ Find the Key with the Maximum Value in a Dictionary

my_dict = {'a': 10, 'b': 50, 'c': 20}

max_key = max(my_dict, key=my_dict.get)

print(f"The key with the highest value is: {max_key}")




