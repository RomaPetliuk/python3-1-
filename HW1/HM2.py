Usergrade = int(input("Ведите свою оценку: "))

if Usergrade > 0 and Usergrade <= 49:
    print("Незадовольнительно")
elif Usergrade >= 50 and Usergrade <= 69:
    print("Нормально")
elif Usergrade >= 70 and Usergrade <= 89:
    print("Хорошо")
else:
    print("Отлично")