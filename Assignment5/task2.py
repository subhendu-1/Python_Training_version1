class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

class FuelVehicle:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

class HybridVehicle(ElectricVehicle, FuelVehicle):
    def __init__(self, battery_capacity, fuel_type):
        ElectricVehicle.__init__(self, battery_capacity)
        FuelVehicle.__init__(self, fuel_type)

    def get_info(self):
        return f"Battery: {self.battery_capacity}kWh, Fuel: {self.fuel_type}"

# Example
hv = HybridVehicle(80, "Petrol")
print(hv.get_info())
