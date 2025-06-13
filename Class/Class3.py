# protected is prefix with _
# private is prefix with _ _


# static metod does not take self or cls



# class Employee:
#     @classmethod
#     def sample(cls,message):
#         cls.message = message
    
#     @staticmethod

#     def IncreaeCount():
#         print("Count Incremented")
#         print(id)

#     def __init__(subhendu,id,name):
#         subhendu.id = id
#         subhendu.name = name
    

# print(Employee.company)
# Employee.company = "Version 1"

# first_employee = Employee(20,"Subhendu")
# print(first_employee.id)
# print(first_employee.name)

# first_employee.id = 201

# print(first_employee.id)
# print(first_employee.name)

# second_employee = Employee()

# second_employee.id = 200
# second_employee.name = "Rajat"

# print(second_employee.id)
# print(second_employee.name)















class Employee:
    company="Version"
    __count = 0
    def __init__(self,id,name):
        self.id = id
        self.name = name
        # Employee.count +=1
 
    @classmethod
    def get_count(cls):
        return cls.count
       
   
class Math:
    @staticmethod
    def add(a,b):
        return a+b
   
    @staticmethod
    def subtract(a,b):
        return a-b
   
print(Employee.company)
Employee.company="Version 1"
 
first_employee = Employee(101,"Ram")
print(first_employee.id)
print(first_employee.name)
print(first_employee.company)
 
second_employee= Employee(102,"Venu")
print(second_employee.id)
print(second_employee.name)
print(second_employee.company)

print(Employee.__count)
print(Employee.get_count())


