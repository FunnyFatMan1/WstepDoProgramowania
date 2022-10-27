x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
if y < x:
    x,y = y,x
while x <= y:
    print(x, end=" ")
    x += 1