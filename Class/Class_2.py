from functools import reduce
a = 10
b = 20

a,b = b, a + 20
print(a,b,sep = ",", end = "!")
print("Hello")
# print(a)

# frouit = ["Mango","Guava",292,'s',True]

frouit = ("Mango","Guava",292,'s',True)

# frouit[1] = "apple"

# frouit.append("Strawbarry")

# frouit.insert(8,"BlueBarry")

print(frouit[1:4])

for i in frouit:
    print(i)


employee = {
    "id" : 1,
    "name" : "Subhendu",
    "dept" : "IT",
    "salary" : 2000,
    # "name" : "Jhon"
}

employee["dept"] = "Manager"


print(employee["name"])
print(employee.get("name"))
# for i in employee.Value():
#     print(i)


for key, Value in employee.items():
    print(f"{key} : {Value}")


def sayHello(name = ""):
    print(f"hi hallo {name}")

sayHello("Subhendu")
sayHello()



def add(*args):
    print(type(args))
    return sum(args)

print(add(20,30))


def Printdata(**kargs):
    for key,value in kargs:
        print(f"{key} : {value}")

# Printdata()

# lambda function: When single expression we use it

square = lambda x : x*2
print(square(5))

substract = lambda a,b : a - b
print(substract(70,10))

number = [10,20,30]
squared = list(map(lambda a:a**2,number))

print(number)
print(squared)

# LOGGER 

def log_to_console(message):
    print(f"[CONSOLE] {message}")

def log_to_file(message):
    print(f"[FILE] {message}")

def log(message,handler_func):
    handler_func(message)

log("Server Started",log_to_console)
log("Error Occoured",log_to_file)

# def create_multiplier(n):
#     def multiplier(x):
#         return x*n
#     return multiplier

# create_multiplier(5)
# print(multiplier(4))



numbers = [1,2,4,5]
print(reduce(lambda a,b: a + b,numbers))
