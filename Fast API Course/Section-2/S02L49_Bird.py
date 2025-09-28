from S02L49_Animal import *

class Bird(Animal):
    def __init__(self):
        super().__init__(1, 'Green', 5, 'Bird')

    def talk(self):
        print('Chirp')

    def fly(self):
        print(f'{self.animal_type} is flying.')