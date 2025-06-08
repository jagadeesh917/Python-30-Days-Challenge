class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Tata", "Nexon", 2023, "Red")

car1.display()
print()
car2.display()

