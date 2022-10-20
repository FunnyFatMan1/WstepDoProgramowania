wiek=int(input("Podaj wiek: "))

if wiek< 0:
    print("Prosze podac proawidlowy wiek")
elif wiek<4 :
    print("Wstęp Bezpłatny")
elif wiek >4 and wiek <18:
    print("Cena biletu: 10zł")
else :
    print("Cena biletu: 20zł")

