import random
cNumber = random.randint(1, 10)
tries = 3

for i in range(tries):
    userNum = int(input("Введіть загадане число (1 - 10) "))

    if userNum == cNumber:
        print(F"Ти переміг число, справді було -- {cNumber}")
        break
    if userNum < cNumber:
        print("Більше")
    elif userNum > cNumber:
        print("Меньше")
    else:
        print("Ти переміг")
else:
    print(F"У вас закінчилися спроби, загадане число було -- {cNumber}")