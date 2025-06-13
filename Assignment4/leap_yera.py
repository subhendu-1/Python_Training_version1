# 5️⃣ Check if a Given Year is a Leap Year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = 2025
print(f"Is {year} a leap year? {is_leap_year(year)}")
