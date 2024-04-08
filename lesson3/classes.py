class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f'{self.year} {self.make} {self.model}')


# Inheritance in Python
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def print_info(self):
        print(f'{self.year} {self.make} {self.model} with {self.doors} doors')
  
my_car = Car('Toyota', 'Corolla', 2015, 4)


class Truck(Vehicle):
    def __init__(self, make, model, year, bed_type):
        super().__init__(make, model, year)
        self.bed_type = bed_type

    def print_info(self):
        print(f'{self.year} {self.make} {self.model} with {self.bed_type} bed')

my_truck = Truck('Ford', 'F150', 2018, 'short')

my_truck.bed_type = 'long'

my_truck.print_info()

my_car.print_info()
print(isinstance(my_car, Car))

print('\n\n')

for v in [my_car, my_truck]:
    v.print_info()
    # print(isinstance(v, Vehicle))
    # print(isinstance(v, Car))
    # print(isinstance(v, Truck))
    # print(isinstance(v, object))
    print('\n')
