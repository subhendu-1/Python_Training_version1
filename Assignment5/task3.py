class Animal:
    def breathe(self):
        return "Breathing"

class Mammal(Animal):
    def warm_blooded(self):
        return "Warm-blooded"

class Dog(Mammal):
    def bark(self):
        return "Barking"

# Example
dog = Dog()
print(dog.breathe())
print(dog.warm_blooded())
print(dog.bark())
