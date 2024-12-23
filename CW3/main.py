from CW5.classes import Berserk
from CW5.classes import Tank
from HW5.classAssasin import Assassin


player1 = Berserk("Andrey", 500, 50, 10)
player1.print_stats()

player2 = Assassin("Roma", 300, 75, 30)
player2.print_stats() 

player3 = Tank("Ekaterina", 1500, 15, 50)
player3.print_stats()


while player1.health > 0 and player2.health > 0 and player3.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} атакував {player2.name} і наніс {player1_damage} шкоди")
    print(f"у {player2.name} лишилося {player2.health} здоров\'я")
    print('')
    player2_damage = player2.attack(player3)
    print(f"{player2.name} атакував {player3.name} і наніс {player2_damage} шкоди")
    print(f"у {player3.name} лишилося {player3.health} здоров\'я")
    print('')
    player3_damage = player3.attack(player1)
    print(f"{player3.name} атакував {player1.name} і наніс {player3_damage} шкоди")
    print(f"у {player1.name} лишилося {player1.health} здоров\'я")
    print('')
print("\n\n")
player1.print_stats()
player2.print_stats()
player3.print_stats()