import random

def list():
    a = [random.randint(0,30) for i in range(10)]
    print(a)
    b = [random.randint(0,30) for i in range(10)]
    print(b)
    c= []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
                break
    print(c) 
list()
