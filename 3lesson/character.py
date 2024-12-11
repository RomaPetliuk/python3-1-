class Character:
    name = ""
    health = 100
    damage = 5
    defence = 0

    def print_ststs(self):
        print(f'-< {self.name}>-')
        print(f" HP: {self.health}")
        print(f" Damage: {self.damag}")
        print(f" defence: {self.defence}")