from S02L49_Animal import *

class Dog(Animal):
    def __init__(self, weight: int, color: str, age: int, can_shed: bool, domestic_name: str):
        super().__init__(weight, color, age, "Dog")
        self.can_shed: bool = can_shed
        self.domestic_name: str = domestic_name

    def talk(self):
        print('Dog is barking!')

    def eat(self):
        print('Chews on bone.')
