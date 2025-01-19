from FEP1 import Person
human = Person(name='Тарас', money=0, mood=100, health=100)

print(human)

human.change_state(
         money = 100,
         mood = -20,
         health = -5
     )

print(human)
print((()))