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
srednia=0
mniejszy=0
wiekszy=0
punkty=[]
x=1
while x <= 15:
    punkty.append(random.randint(0,50))
    x+=1
print(punkty)
punkty.sort()

print(punkty.min())
print(punkty.max())
for y in range (15):
    srednia +=punkty[y] #zliczanie łącznie ilości punktów
liczba=int(input("podaj liczbe: "))
for m in range (15):
    if liczba not in punkty:
        print("nie ma takiej liczby")
        break
    elif liczba ==punkty[m]:
        print(m)
sredniar=srednia/15
print(sredniar) # sredniar to suma ptk przez ilosc osob
for z in range (15):
    if punkty[z] < sredniar :
        mniejszy+=1
    elif punkty[z] > sredniar:
        wiekszy+=1
print(f"Tyle było osób poniżej średniej {mniejszy} , a tyle powyżej {wiekszy}")


