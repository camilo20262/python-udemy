def suma():
    num1= int(input("Ingrese el primer número: "))
    num2= int(input("Ingrese el segundo número: "))
    print(num1+num2)

try:
    suma()
except ValueError:
    print("Algo malo sucedio  en el programa")
except TypeError:
    print("estas intenando concatenar cosas que no son numeros")
else:
    print("hiciste todo bien")
finally:
    print("El programa ha finalizado")




def pedir_numero():
    while True:
        try:
            num= int(input("Ingresa un número entero: "))
        except ValueError:
            print("Eso no es un número entero. Por favor, intenta de nuevo.")
        else:
            print("Ingresaste el número ",num )
            break
    print("Gracias por ingresar un número entero:", num)

pedir_numero()