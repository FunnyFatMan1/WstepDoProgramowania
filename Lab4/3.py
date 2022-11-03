'''Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście'''

zwierzeta=[]
zwierzeta.append('kot')
zwierzeta.append('pies')
zwierzeta.append('łoś')
zwierzeta.append('ryba')
zwierzeta.append('chomik')
zwierzeta.append('żubr')
zwierzeta.append('małpa')
zwierzeta.sort()
print(f"lista posortowana{zwierzeta}")
print(zwierzeta[0])
print(zwierzeta[-3:])
print(len(zwierzeta))
