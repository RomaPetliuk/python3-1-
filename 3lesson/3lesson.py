from character import Character

player1 = Character("Andrei", 2400, 200, 50)
player1.print_stats()

player2 = Character("Roma", 2000, 300, 0)
player2.print_stats()

player3 = Character("Katia")
player3.print_stats()

player1.attack(player2)

print("\n\n")
player1.print_stats()
player2.print_stats()