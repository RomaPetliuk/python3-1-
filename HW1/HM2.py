userGrade = int(input("Please input your grade: "))

if 0 <= userGrade <= 49:
    print("Bad")
elif 50 <= userGrade <= 69:
    print("Mid")
elif 70 <= userGrade <= 89:
    print("Good")
else:
    print("Great")