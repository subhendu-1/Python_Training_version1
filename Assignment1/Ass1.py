a = 12
b = 5
c = '7'
d = True

if d:
    res = (a+b) * int(c)


if res % 2 == 0:
    shifted_value = res >> 2
else:
    shifted_value = res << 1

div = b | a
final_value = shifted_value // div

arr = [10,20,30,40]

passed_value = (final_value >= a) or (final_value in arr)


print("Final Value is : ",final_value)
print("Checking Passed: ",passed_value)


