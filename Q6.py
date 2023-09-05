class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):

        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

my_car = Car("Toyota", "Camry", 2022)

electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)

print("Car Information:")
my_car.display_info()

print("\nElectric Car Information:")
electric_car.display_info()
