# Parent class
class Car:
    def __init__(self, brand, model, color, sub_class):
        self.brand = brand
        self.model = model
        self.color = color
        self.sub_class = sub_class

    def car_details(self):
        print("Car Attributes:")
        print(f"  Brand     : {self.brand}")
        print(f"  Model     : {self.model}")
        print(f"  Color     : {self.color}")
        print(f"  Subclass  : {self.sub_class}")

# Child class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, color, sub_class, battery):
        super().__init__(brand, model, color, sub_class)
        self.battery = battery

    def car_details(self):
        print("Electric Car Attributes:")
        super().car_details()  # Print base attributes
        print(f"  Battery   : {self.battery}")  # Print additional attribute

# Create objects
my_car = Car('Tata Motors', 'Harrier', 'Oberon Black', 'XZ+')
extended_car = ElectricCar('Mahindra', 'XUV400 EV', 'Napoli Black', 'EL Pro', '39.4kWh')

# Print all attributes
print("\n-- Car_Details --")
my_car.car_details()

print("\n-- Electric_Car_Details --")
extended_car.car_details()
