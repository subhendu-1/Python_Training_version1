class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"

# Example
m = Manager("Alice", 101, 5)
print(m.get_details())
