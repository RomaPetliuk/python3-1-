from CW3.character import Character
import random

class Assassin(Character):
    def __init__(self, name,health=250, damage=25, defence=10):
        Character.__init__(self, name, health, damage, defence)

    def attack(self, target):
        attackNum = random.randint(1, 100)
        if attackNum <= 40:
            critical_damage = 1000
            return target.take_damage(critical_damage)
        else:
            return super().attack(target)

    def take_damage(self, damage):
        defNum = random.randint(1, 10)
        if defNum >= 5:
            final_damage = damage - self.defence if damage >= self.defence else 0
            self.health = max(self.health - final_damage, 0)
            return final_damage
        else:
            final_damage = damage + self.defence
            self.health = max(self.health - final_damage, 0)
            return final_damage