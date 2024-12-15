from lesson3.character import Character
class Berserk(Character):
    def __init__(self, name, health=1000, damage=200, defense=0):
        Character.__init__(self, name, health, damage, defense)