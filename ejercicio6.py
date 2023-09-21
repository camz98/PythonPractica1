edad=int(input("Dime tu edad: "))
if edad<4:
    print("entrada gratis")
elif edad>=4 and edad<=18:
    print("precio de entrada: 5 soles")
elif edad>18:
    print("precio de entrada: 10 soles")
