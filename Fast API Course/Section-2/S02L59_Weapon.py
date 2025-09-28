class Weapon:
    def __init__(self, weapon_type: str, attack_increase: int):
        self.__weapon_type = weapon_type
        self.__attack_increase = attack_increase

    def get_weapon_type(self):
        return self.__weapon_type

    def get_attack_increase(self):
        return self.__attack_increase
