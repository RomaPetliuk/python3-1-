from lesson5.berserk import Berserk
from character import Character


player1 = Character("Andrey", 110, 7, 0)
player1.print_stats()

player2 = Berserk("Gde Krishichka", 100, 15, 0)
player2.print_stats()

player3 = Character("Ekaterina Mezylina", 100, -10, -5)
player3.print_stats()


while player1.health > 0 and player2.health > 0 and player3.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} атакував {player2.name} і наніс {player1_damage} шкоди")
    print(f"у {player1.name} лишилося {player1.health} здоровя")
    player2_damage = player2.attack(player3)
    print(f"{player2.name} атакував {player3.name} і наніс {player2_damage} шкоди")
    print(f"у {player3.name} лишилося {player3.health} здоровя")
    player3_damage = player3.attack(player2)
    print(f"{player3.name} атакував {player2.name} і наніс {player3_damage} шкоди")
    print(f"у {player2.name} лишилося {player2.health} здоровя")
print("\n\n")
player1.print_stats()
player2.print_stats()
player3.print_stats()