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

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        self.mood += mood
        self.money += money
        if self.health < 0:
            raise ValueError("Person died.")
        if self.mood < 0:
            raise ValueError("Person became depressed.")
        if self.money < 0:
            raise ValueError("Person went bankrupt.")
