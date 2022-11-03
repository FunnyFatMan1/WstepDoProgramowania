'''
Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej
'''
import random
punkty=[]
x=1
while x <= 15:
    punkty.append(random.randint(0,50))
    x+=1
print(punkty)
punkty.sort()

print(punkty[0])
print(punkty[14])
liczba=int(input("podaj liczbe: "))
if liczba in punkty:
    print(liczba)
else:
    print('nie ma takiej liczby :( ')

