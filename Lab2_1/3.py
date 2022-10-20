'''Zadanie 3 (3.py) Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
dzielić oraz obliczać potęgę.
Przykład: Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: 2
Podaj argument 1: 34
Podaj argument 2: 5
Wynik: 29
'''

print('''
Jaką operację chcesz wykonać? 
 1:Dodawanie 
 2:Odejmowanie 
 3.Monżenie 
 4.Dzielenie 
 5.Potęgowanie 
 6.Wyjście 
''')
option=0



while option==6:
    option = int(input("Jaką operację chcesz wykonać? "))
    if option == 1:
        a = int(input("Podaj a "))
        b = int(input("Podaj b "))
        x= a+b
        print("Wynik: ", x)
    elif option == 2:
        a = int(input("Podaj a "))
        b = int(input("Podaj b "))
        x = a - b
        print("Wynik: ",x)
    elif option == 3:
        a = int(input("Podaj a "))
        b = int(input("Podaj b "))
        x = a * b
        print("Wynik: ",x)
    elif option == 4:
        a = int(input("Podaj a "))
        b = int(input("Podaj b "))
        x = a / b
        print("Wynik: ", x)
    elif option == 5:
        a = int(input("Podaj a "))
        b = int(input("Podaj b "))
        x = a ** b
        print("Wynik: ", x)
