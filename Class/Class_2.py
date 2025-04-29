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

Printdata()