'''
Allow the client to access functionalities without having access to its details.

This allows user to not have to understand what the functionality is behind the scenes.
'''

from S02L41_Enemy import *

enemy = Enemy()

enemy.type_of_enemy = 'Zombie'
enemy.present()
enemy.talk()
enemy.walk_forward()
enemy.attack()
