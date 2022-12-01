'''Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę'''

def z3(*args):
    print(type(args),(args))
    for x in args:
        print(x)

#z3()# wywołujemy to aby pokazać że nie ważne ile parametrów podamy to i tsk funkcja zwróci nam krotkę
#z3(1,1.5,False,"jeden",[1,2,3,4])


def z3_1(*args):
    zmienna = args[0]
    for x in args[1:]:
        if x > zmienna:
            zmienna = x

    print(f'największa liczba w krotce wynosi: {zmienna}')


z3_1(1,2,3,10,100,17,18,99)

def maxf(number1,*args):
    zmienna = number1
    for x in args[1:]:
        if x > zmienna:
            zmienna = x

    print(f'największa liczba w krotce wynosi: {zmienna}')


maxf(678,2,3,10,234,17,18,99)

