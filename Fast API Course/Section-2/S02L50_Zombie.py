import random
from S02L41_Enemy import *

class Zombie(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__('Zombie')
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print('*Grumbling...*')

    def spread_disease(self):
        print('The zombie is trying to spread infection.')

    def special_attack(self):
        did_special_attack_work = random.random() < .2
        if (did_special_attack_work):
            self.attack_damage += 2
            print(f'{self.get_type_of_enemy()} attack has increased by 2.')