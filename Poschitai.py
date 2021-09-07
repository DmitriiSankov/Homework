def summa():
    A = int(input("Введите число "))
    summa = 0
    while A > 0:
        digit = A % 10
        summa = summa + digit
        A = A // 10
    print("Cумма элементов числа:",summa )
summa()