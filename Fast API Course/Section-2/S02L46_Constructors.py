from S02L41_Enemy import *

zombie = Enemy("Zombie", 15, 2)
zombie.talk()
zombie.walk_forward()
zombie.attack()

big_zombie = Enemy('Big Zombie', 100, 10)
big_zombie.attack()