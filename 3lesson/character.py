class Character:
    name = ""
    health = 100
    damage = 5
    defense = 0

    def __init__(self, name, health=1000, damage=200, defense=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def print_stats(self):
        print(f" -< {self.name} >- ")
        print(f" Здоров`я {self.health} ")
        print(f" Шкода {self.damage} ")
        print(f" Захист {self.defense} ")

    def take_damage(self, damage, defense):
        self.health = max(self.health - damage + defense, 0)

    def attack(self, target):
        target.take_damage(self.damage, self.defense)