n1=float(input("digita un numero: "))
n2=float(input("digita otro numero: "))
n3=float(input("elige un numero del 1 al 3: "))

if n3==1:
    print(f"suma: {n1+n2}")
elif n3==2:
    print(f"resta: {n1-n2}")
elif n3==3:
    print(f"multiplicacion: {n1*n2}")
else:
    print("opcion no existe")
