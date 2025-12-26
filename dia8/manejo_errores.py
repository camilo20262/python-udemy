def suma():
    num1= int(input("Ingrese el primer número: "))
    num2= int(input("Ingrese el segundo número: "))
    print(num1+num2)

try:
    suma()
except ValueError:
    print("Algo malo sucedio  en el programa")
else:
    print("hiciste todo bien")
finally:
    print("El programa ha finalizado")