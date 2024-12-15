from lesson3.character import Character
class Berserk(Character):
    damage_multiplier = 15
    rage_limit = 60;
    def __init__(self, name, health=1000, damage=200, defense=0, damage_multiplier = 15, rage_limit = 60 ):
        Character.__init__(self, name, health, damage, defense)
        self.damage_multiplier = damage_multiplier
        self.rage_limit = rage_limit

    def attack(self, target):
        final_damage = self.damage * self.damage_multiplier if self.health < self.rage_limit else self.damage
        return target.take_damage(final_damage)

class Tank(Character):
    def __init__(self, name,health=100, damage=20, defence=10):
        Character.__init__(self, name, health, damage, defence)

    def take_damage(self, damage):
        final_damage = damage - self.defence if damage >= self.defence else 0
        self.health = max(self.health - final_damage, 0)
        return final_damage