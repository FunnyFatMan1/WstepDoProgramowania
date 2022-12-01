'''
Zadanie 2. Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania.
'''
def oblicz(l1,l2):
    '''oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania'''
    print(f"{l1} + {l2} = {l1 + l2}")
    print(f"{l1} - {l2} = {l1 - l2}")

x=int(input("podaj liczbe 1: "))
y=int(input("podaj liczbe 2: "))
oblicz(x,y)
print(oblicz.__doc__)