import random

def spisok():
    newlist = [random.randint(0,100) for i in range(10)]
    print(newlist)
    A = int(input("Введите число от 0 до 9:"))
    newlist[A] = A

    print(newlist)
spisok()
