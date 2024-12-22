user1 = 0

def userInt(user1, min_value=None, max_value=None):
    while True:
        try:
            user1 = int(input(f"Ведите число от {min_value} до {max_value}: "))
            if user1 in range(min_value, max_value):
                print("Молодец!!!")
                break
            else:
                print(f"Введите число в диапазоне от {min_value} до {max_value}")
        except ValueError:
            print("Введите именно число!!! ")
        except Exception as pomelka:
            print(f"{type(pomelka)}__--__{pomelka}")
    return user1


userInt(user1, min_value=100, max_value=1000)
