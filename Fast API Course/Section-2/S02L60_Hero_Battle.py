from S02L59_Weapon import *
from S02L59_Hero import *
from S02L41_Enemy import *


def battle(hero: Hero, enemy: Enemy):
    print('\n----------')
    hero.talk()
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:
        # hero.special_attack()
        enemy.special_attack()

        hero.attack()
        enemy.health_points -= hero.attack_damage

        enemy.attack()
        hero.health_points -= enemy.attack_damage

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'Enemy wins!')


hero: Hero = Hero(attack_damage=10, health_points=100)
sword:Weapon = Weapon("Sword", 5)
hero.equip_weapon(sword)

enemy: Enemy = Enemy("Enemy", attack_damage=10, health_points=100)

battle(hero, enemy)
