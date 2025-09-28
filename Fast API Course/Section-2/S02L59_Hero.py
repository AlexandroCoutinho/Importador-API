from S02L59_Weapon import *


class Hero:
    def __init__(self, health_points: int, attack_damage: int):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None

    def equip_weapon(self, weapon:Weapon):
        print("Equipping weapon")
        print(self.weapon is not None)
        if self.weapon is None and not self.is_weapon_equipped:
            self.weapon = weapon
            self.attack_damage += self.weapon.get_attack_increase()
            self.is_weapon_equipped = True
            print("Weapon is equipped")

    def talk(self):
        print("I'll save the world!")

    def attack(self):
        print(f'Hero is attacking for {self.attack_damage} points.')
