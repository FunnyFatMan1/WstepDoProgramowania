'''
Napisz funkcję o dwóch parametrach, imię oraz wiek, która wypisze ich wartości na ekranie.
• Dodaj w następnej linii po nagłówku funkcji komentarz opisujący działanie funkcji. Wyświetl ten opis za
pomocą instrukcji
print(nazwa_funkcji.__doc__)
• Jeśli w wywołaniu funkcji nie podano wieku, przypisz do parametru wiek wartość domyślną 20.
Uwaga: Parametry z wartościami domyślnymi powinny być definiowane jako ostatnie na liście
parametrów, ponieważ Python dopasowuje argumenty do parametrów na podstawie ich pozycji:
def fun(param1, param2=default2, param3=default3)

'''
def funkcja(imie, wiek):
    '''funkcja wypisze moję imię oraz wiek'''
    print(f"Witaj, {imie} , ile ty masz lat? {wiek}")




funkcja("Kacper","17")
print(funkcja.__doc__)


