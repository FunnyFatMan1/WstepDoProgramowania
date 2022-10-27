'''
) Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue
'''
x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
if y < x:
    x,y = y,x
while x <= y:
    if x % 2 == 1:
        x +=1
        continue
    print(x, end=", ")
    x += 1


