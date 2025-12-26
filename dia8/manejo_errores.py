def suma():
    num1= int(input("Ingrese el primer número: "))
    num2= int(input("Ingrese el segundo número: "))
    print(num1+num2)

try:
    suma()
except:
    print("Algo malo sucedio  en el programa")

finally:
    print("El programa ha finalizado")