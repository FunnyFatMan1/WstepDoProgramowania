'''
• Wypisz wszystkie pary klucz:wartość występujące w słowniku:
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
• Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
Wskazówki:
− przejdź za pomocą pętli po kluczach zapisanych w liście;
− następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
klucz:wartość) do nowego słownika.
• Usuń ze słownika wartości, których klucze występują w liście.
• Sprawdź, czy wartość „Jones” występuje w słowniku.
• Zmień w słowniku klucz ‘city’ na ‘location’.

'''
dict1 = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for k,y in dict1.items():
    print(f'{k:<8} = {y:>8}')

list1=['salary', 'city']
dict2={}
for k,y in dict1.items():
    if k in list1:
        print(k, y)
        dict2[k]=y
# inny sposob
#D = {k:sample_dict[k] for k in list if k in sample_dict.keys()}

for k in dict2.keys():
    dict1.pop(k,None)
print(dict1)

if "Jones" in dict1.values():
    print('element znajduje sie w słowniku')
else:
    print('nie ma ')

dict2['location'] = dict2['city']
del dict2['city']

print(dict2)

