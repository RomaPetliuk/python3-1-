from FEP1 import Person
from FEP1 import Action
import random
human = Person(name='Roma', money=0, mood=100, health=100)

human.change_state(
         money = 100,
         mood = -20,
         health = -5
     )

peoples = [
    Person(name="Roma", money = 500, mood = 100, health = 80),
    Person(name="Marina", money = 100, mood = 150, health = 100),
    Person(name="Vova", money = 50000, mood = 100, health = 90)
]
actions = [
    Action("Робота", money=random.randint(10, 50), health=random.randint(-10, -5), mood=random.randint(-10, -3)),
    Action("Відпочинок", money=random.randint(-15, -5), health=random.randint(1, 5), mood=random.randint(1, 5)),
]
while True:
    for person in peoples:
        person.change_state(
            money = random.randint(-10, -5),
            mood = random.randint(-10, -5),
            health = random.randint(-10, -5)
        )
        if person.health <= 0:
            peoples.remove(person)
        if person.mood <= 0:
            peoples.remove(person)
        if person.money <= 0:
            peoples.remove(person)

        if len(peoples) == 0:
            print("persons are empty")
            break
