a = float(input("Введіть значення a = "))
b = float(input("Введіть значення b = "))
UserS = input("Введите знак (+, -, *, /) ")

if UserS == "+":
    result = a + b
    print("a + b =",result)
if UserS == "-":
    result = a - b
    print("a - b =", result)
if UserS == "*":
    result = a * b
    print("a * b =", result)
if UserS == "/":
    if b == 0:
        print("На 0 ділити не можна")
    else:
        result = a / b
        print("a / b =", result)
        print(round(result))