'''
Zadanie 6.
• Załóżmy, że lista X składa się z 10 elementów. Przenieś ostatnie trzy elementy z końca na początek listy
bez zmiany ich oryginalnej kolejności.
• Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y. Wyświetl obie listy
na ekranie.
'''
x=list(range(10))
x[:0]=x[-3:]
#del.x[-3:] tak tez moze byc
x[-3:]=[]
print(x)
y=x[:]
y[2]=1000000
print(y)
print(x)