'''
Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
wykorzystaniem pętli while
'''
n=int(input('Podaj ilosc studentow: '))
x=1
b=0
while x <= n:
    a=int(input(f'podaj punkty {x} studenta'))
    b += a
    x += 1

srednia= b/n
print('Srednia wszystkich studentow'srednia)