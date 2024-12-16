from character import Character
from lesson5.classes import Berserk

player1 = Character("Andrey trubochist", 110, 7, 0)
player1.print_stats()

player2 = Berserk("Gde Krishichka", 100, 15, 0)
player2.print_stats()

player3 = Character("Ekaterina Mezylina", 100, -10, -5)
player3.print_stats()


while player1.health > 0 and player2.health > 0 and player3.health > 0:
    player1.attack(player2)
    player1.attack(player3)
    player2.attack(player1)
    player2.attack(player3)
    player3.attack(player2)
    player3.attack(player1)
    print("\n\n")
    player1.print_stats()
    player2.print_stats()
    player3.print_stats()