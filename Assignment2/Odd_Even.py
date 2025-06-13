# 7. Odd or Even Counter
# Input 5 numbers one by one (use loop).
# Count how many are odd, how many are even.

even_cnt = 0
odd_cnt = 0

for count in range(5):
    num = int(input())
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print(f"Even number count is {even_cnt}")
print(f"Odd number count is {odd_cnt}")




