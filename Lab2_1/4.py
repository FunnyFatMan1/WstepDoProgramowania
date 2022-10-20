litera=input("Wpisz litere: ")
roznica=ord('a')-ord('A')
if 'a' <= litera <= 'z' :
    print(chr(ord(litera) - roznica) )

elif 'A' <= litera <= 'Z' :
    nowa=ord(litera) + roznica
    znak=chr (nowa)
    print(znak)
else:
    print("nie jest to  litera")

#ord(znak)-zwraca kod ASCII
#chr(kod)-zwraca znak
