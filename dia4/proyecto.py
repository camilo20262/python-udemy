from random import *
nombre=input("Ingrese su nombre: ")
intentos=0
numero_secreto= randint(1,100)#genera un numero aleatorio entre 1 y 100
print("""
Bienvenido al juego de adivinar el numero
Tienes 8 intentos para adivinar el numero secreto""")
while intentos <8:
    numero=int(input("ingresa el numero para adivinar: "))
    intentos+=1
    print(f"Intento numero: {intentos}")
    if intentos==8:
        print(f"Lo siento {nombre} has agotado tus intentos, el numero secreto era {numero_secreto}")
        break
    match numero:
        case numero if numero <=0 or numero>100:
            print("El numero debe estar entre 1 y 100")
        case numero if numero < numero_secreto:
            print(f"El numero {numero} es menor al numero secreto ")
        case numero if numero > numero_secreto:
            print(f"El numero {numero} es mayor al numero secreto ")
        case numero if numero == numero_secreto:
            print(f"Felicidades {nombre} has adivinado el numero secreto {numero_secreto} en {intentos} intentos")
            break
        case _:
            print("Error inesperado")