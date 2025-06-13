class Device:
    def __init__(self, brand):
        self.brand = brand

class Mobile(Device):
    def mobile_feature(self):
        return "Touchscreen"

class Laptop(Device):
    def laptop_feature(self):
        return "Keyboard"

class HybridDevice(Mobile, Laptop):
    def get_specs(self):
        return f"Brand: {self.brand}, Features: {self.mobile_feature()}, {self.laptop_feature()}"

# Example
hd = HybridDevice("TechCorp")
print(hd.get_specs())
