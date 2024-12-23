try:
    result = []

    def divider(a, b):
        if a < b:
            raise ValueError(f"a cannot be less than b!!!, a = {a}, b = {b}")
        if b > 100:
            raise IndexError(f"b cannot be more than 100!!!, b = {b}")
        return a/b

# Ето 1 проект там где все как в задании (ДЗ).

    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4, 300: 200}

    for key in data:
        try:
            res = divider(key, data[key])
            result.append(res)
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except IndexError as ie:
            print(f"IndexError: {ie}")
        except ZeroDivisionError as zde:
            print(f"ZeroDivisionError: {zde}")
        except TypeError as te:
            print(f"TypeError: {te}")
        except Exception as e:
            print(f"Other Exception: {e}")

    print(result)
except Exception as e:
    print(f"Exceptions: {e}")
