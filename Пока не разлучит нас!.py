def function_while():
    A = int(input("Введите первое число 'A' "))
    B = int(input("Введите второе число 'B' "))
    C = int(input("Введите третье число 'C' "))
    while A<=B:
        A=A+C
        if A<B:
           print("Число " + str(A) + " Меньше " + str(B))
        elif A==B:
           print("Число " + str(A) + " Равно " + str(B))
        else:
            print("Поздравляем!" + " Число " + str(A) + " Больше " + str(B))
function_while()