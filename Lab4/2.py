'''
Zadanie 2.
• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę
'''
import random
zestaw_1=[]
x=1
ilosc=int(input('podaj ilość liczb w liscie: '))
while x <=ilosc:
    zestaw_1.append(random.randint(1,10))
    x+=1

ilosc2=int(input('podaj ilość liczb w liscie: '))
zestaw_2 = []
y = 1
while y <= ilosc2:
    zestaw_2.append(random.randint(5, 15))
    y += 1

print(f"lista1 {zestaw_1}, druga lista{zestaw_2}")

liczba=int(input('Podaj liczbe: '))
if liczba in zestaw_1:
    print('Liczba z zestawu1')
elif liczba in zestaw_2:
    print('Liczba z zestawu2')
else:
    print('Nie ma takiej liczby w obu zestawach')

zestaw_1_2=zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)


