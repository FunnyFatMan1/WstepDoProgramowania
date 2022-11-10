'''Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście'''

zwierzeta=[]
for x in range (6):
    x=input("Podaj zwierze:")
    zwierzeta.append(x)

zwierzeta.sort()
print(f"lista posortowana{zwierzeta}")
print(zwierzeta[0])
print(zwierzeta[-3:])
print(len(zwierzeta))
