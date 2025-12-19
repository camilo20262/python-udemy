from calendar import c


def saludar_persona(nombre):
    print("Hola, como estas? "+nombre)

saludar_persona("Camila")

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
bienvenida("Andres")



def cuadrado(un_numero):
    return un_numero**2

valor=cuadrado(5)
print(valor)
