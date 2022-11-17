liczba1 = input("Podaj liczbę: ")
liczba2 = input("Podaj liczbę: ")
nadpisanie = 0
temp = 0
roznica = 0
wynik = ''
wynikkon = ''
len1 = len(liczba1)
len2 = len(liczba2)
leno = 0

if len1 == len2:
    leno = len1
elif len1 > len2:
    leno = len1
    roznica = len1 - len2
    liczba2 = ("0" * roznica) + liczba2
elif len1 < len2:
    leno = len2
    roznica = len2 - len1
    liczba1 = ("0" * roznica) + liczba1

for x in range(1, leno + 1):
    temp = int(liczba1[-x]) + int(liczba2[-x])
    if nadpisanie == 1:
        temp += 1

    if temp > 9:
        nadpisanie = 1
        temp -= 10
    elif temp <= 9:
        nadpisanie = 0
    wynik = wynik + str(temp)

    if x == leno:
        wynik = wynik[::-1]
        if nadpisanie == 1:
            wynikkon = '1' + wynik
        else:
            wynikkon = wynik

print(f"końcowy wynik dodawania pisemnego to: {wynikkon}")













