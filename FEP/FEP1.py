import random


class Action:
    def __init__(self, name, ac_money, ac_health, ac_mood):
        self.name = name
        self.money_change = ac_money
        self.health_change = ac_health
        self.mood_change = ac_mood


class Person:
    name = ""
    health = 100
    mood = 75
    money = 60

    def __init__(self, name, health=100, mood=75, money=10):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'{self.name} (health:{self.health},' \
               f' mood:{self.mood},' \
               f' money: {self.money})'
    def do(self, action: Action):
        self.money += action.money
        self.health += action.health
        self.mood += action.mood

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        self.mood += mood
        self.money += money
        if self.health < 0:
            print("Person died.")
        if self.mood < 0:
            print("Person became depressed.")
        if self.money < 0:
            print("Person went bankrupt.")
        act = random.choice(['work', 'rest'])

        if act == 'work':
            self.money += random.randint(10, 100)
            self.health -= random.randint(5, 10)
            self.mood -= random.randint(20, 40)
        elif act == 'rest':
            self.money -= random.randint(5, 20)
            self.health += random.randint(1, 5)
            self.mood += random.randint(1, 5)