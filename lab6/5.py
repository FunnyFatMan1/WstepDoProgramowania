'''
Napisz program, który połączy dwa słowniki. Dla kluczy występujących w obu słownikach dodaj
wartości.

'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 100, 'd':400}
d3={}
for k in d1.keys():
    for k1 in d2.keys():
        if k==k1:


