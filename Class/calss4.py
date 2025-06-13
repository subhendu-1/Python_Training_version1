class Math:

    def add(self,a,b):
        return a+b 

    # def add(self,a,b,c):
    #     return a+b 

    # def add(self,a,b,c,d):
    #     return a+b
# MyMath = Math()
# MyMath1 = Math()
# print(MyMath.add(3,4))
# print(MyMath.add(3,4,2))
# print(MyMath + MyMath1)

# add(3,5,6)


class FileLogger:
    def write(self, message):
        print('File Logger : ' + message)
 
class ConsoleLogger:
    def write(self, message):
        print('Console Logger : ' + message)
 
class DatabaseLogger:
    def write(self, message):
        print('Database Logger : ' + message)
 
 
def log_message(logger, message):
    logger.write(message)
 
filelog=FileLogger()
conlog=ConsoleLogger()
dblog=DatabaseLogger()
 
log_message(filelog, 'File log message')
log_message(conlog, 'Console log message')
log_message(dblog, 'Database log message')  


class Parent:
    def __init__(self):
        self.value = 100
 
    def show(self):
        print(f"Parent value: {self.value}")
 
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 200
 
    def show(self):
        print(f"Child value: {self.value}")
        super().show()
 
c = Child()
c.show()

def divide(x, y):
   try:
       # Floor Division : Gives only Fractional
       # Part as Answer
       result = x // y
   except ZeroDivisionError:
      print("Sorry ! You are dividing by zero ")
   else:
      print("Yeah ! Your answer is :", result)
   finally: 
       # this block is always executed 
       # regardless of exception generation. 
       print('This is always executed')

divide(20,0) 


import os
 
try:
    if os.path.exists("sample.txt"):
        print("File already exists.")
 
    with open("sample.txt", "a") as f :
        f.write("Hello, World!")
   
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
else:
    print("File opened successfully.")
 