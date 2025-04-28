class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f'This {self.name} is eating')

    def sleep(self):
        print(f'This {self.name} is sleeping')


class Mammal(Animal):
    def __init__(self, name, age, species,is_warm_blooded):
        super().__init__(name, age, species)
        self.is_warm_blooded = is_warm_blooded

    def give_birth(self):
        print(f'This {self.name} is giving birth')
    
    def make_sound(self):
        print('Trumpet sound')


class Bird(Animal):
    def __init__(self, name, age, species,can_fly):
        super().__init__(name, age, species )
        self.can_fly = can_fly

    def lay_eggs(self):
        print(f'This {self.name} is laying eggs')

    def make_sound(self):
        print('Screech sound')

class Reptile(Animal):
    def __init__(self, name, age, species,is_cold_blooded):
        super().__init__(name, age, species)
        self.is_cold_blooded = is_cold_blooded

    def shed_skin(self):
        print(f'This {self.name} is shedding skin now')

    def make_sound(self):
        print('Hissing sound')




class ZooKeeper:
    def __init__(self):
        self.animals = []  # List to store all animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def count_animals(self):
        mammal_count = 0
        bird_count = 0
        reptile_count = 0

        for animal in self.animals:
            if isinstance(animal, Mammal):
                mammal_count += 1
            elif isinstance(animal, Bird):
                bird_count += 1
            elif isinstance(animal, Reptile):
                reptile_count += 1

        print(f'The zoo has:')
        print(f'{mammal_count} Mammals')
        print(f'{bird_count} Birds')
        print(f'{reptile_count} Reptiles')

elephant = Mammal('Elephant',45,'African Elephant',True)
eagle = Bird('Eagle',25,'Bald Eagle',True)
snake = Reptile('Snake',23,'King Cobra',True)


zookeeper = ZooKeeper()

# Add animals to ZooKeeper
zookeeper.add_animal(elephant)
zookeeper.add_animal(eagle)
zookeeper.add_animal(snake)
# Count the animals
zookeeper.count_animals()

# Call some methods to test
elephant.sleep()
eagle.make_sound()
snake.shed_skin()