fruits = ["apple", "orange", "banana", "cherry", "water melon"]
print(fruits)
"""while True:
    try:
        userF = int(input("Введите индекс фрукта: "))
        if userF in range(len(fruits)):
            print(fruits[userF])
        else:
            print("Введите индекс поменьше")
    except ValueError:
        print("Введите индекс фрукта числом")"""
while True:
    try:
        userF = int(input("Введите индекс фрукта: "))
        print(fruits[userF])
    except ValueError:
        print("Введите индекс фрукта числом")
    except IndexError:
        print("Введите существующий индекс")