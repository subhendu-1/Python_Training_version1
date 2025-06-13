marks = int(input("Enter the Student Marks: "))

if marks < 60:
    print("Fail")
elif marks < 70:
    print("Grade D")
elif marks < 80:
    print("Grade C")
elif marks < 90:
    print("Grade B")
else: 
    print("Grade A")