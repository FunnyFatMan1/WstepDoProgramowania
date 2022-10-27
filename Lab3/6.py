
''' Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
break.'''
n=int(input('Podaj ilosc studentow: '))
x=1
b=0
while x <= n:
    a=int(input(f'podaj ocene {x} studenta'))

    if a<0 and a>100:
        x +=1
        continue
    x += 1
    b += a


srednia= b/n
print(srednia)