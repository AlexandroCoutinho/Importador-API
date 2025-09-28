class Dog:
    legs: int = 4
    ears: int = 2
    type: str = 'Goldendoodle'
    age: int = 5
    color: str = 'yellow'

    def bark(self):
        print(f'{self.type} barking.')