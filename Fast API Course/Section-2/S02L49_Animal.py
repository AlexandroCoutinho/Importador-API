class Animal:
    def __init__(self, weight:int, color:str, age:int, animal_type:str):
        self.weight = weight
        self.color = color
        self.age = age
        self.animal_type = animal_type

    def eat(self):
        print('Animal is eating.')

    def sleep(self):
        print('Animal is sleeping.')