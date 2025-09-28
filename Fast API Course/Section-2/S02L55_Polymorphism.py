from S02L41_Enemy import *
from S02L50_Zombie import *
from S02L50_Ogre import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        e1.special_attack()
        e2.special_attack()

        e1.attack()
        e2.health_points -= e1.attack_damage

        e2.attack()
        e1.health_points -= e2.attack_damage


    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


zombie = Zombie(100, 1)
ogre = Ogre(100, 1)

battle(ogre, zombie)
