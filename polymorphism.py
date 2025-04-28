from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display_info(self):
       pass

    @abstractmethod
    def make_sound(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year,doors):
        super().__init__(brand, year)
        self.doors = doors

    def display_info(self):
         print(f'\nThis {self.brand} was made in {self.year} and it has {self.doors}')

    def start_engine(self):
        print(f"\nThe {self.brand} engine roars to life.")

    def make_sound(self):
        print(f'This {self.brand} has a sound of Peeeeeeeeeeeeepppppppp\n')


class Motorcycle(Vehicle):
    def __init__(self, brand, year,type):
        super().__init__(brand, year)
        self.type = type

    def display_info(self):
        types = ', '.join(self.type) if isinstance(self.type, list) else self.type
        print(f'This {self.brand} was made in {self.year} and it is a {types} motorcycle.')

    def start_engine(self):
        print(f"The {self.brand} engine revs loudly.")

    def make_sound(self):
        print(f'This {self.brand} has a sound of Grrrr grrrr\n')


class Truck(Vehicle):

    def __init__(self, brand, year,capacity):
        super().__init__(brand, year)
        self.capacity = capacity

    def display_info(self):
       super().display_info()
       print(f'The {self.brand} has a capacity of {self.capacity}')

    def start_engine(self):
         print(f"The {self.brand} is the king of the road.\n")

    def make_sound(self):
        print(f'This {self.brand} has a sound of Booooop boopppp\n')



vehicles = [
    Car('Honda',2025,4),
    Motorcycle('Aerox',2025,['Sports','Cruiser']),
    Truck('Gothong Truck',2025,'2 Tons'),
]

for vehicle in vehicles:
    vehicle.display_info()
    vehicle.make_sound()



def start_all_vehicles(vehicles: list[Vehicle]):
    for veh in vehicles:
        veh.start_engine()

start_all_vehicles(vehicles)