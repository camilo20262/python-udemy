
def saludar_persona(nombre):#Función que saluda a una persona por su nombre
    print("Hola, como estas? "+nombre)#Imprime el saludo

saludar_persona("Camila")#Llama a la función con el nombre "Camila"

def bienvenida(nombre_persona):#Función que da la bienvenida a una persona
    print(f"¡Bienvenido {nombre_persona}!")#Imprime el mensaje de bienvenida
bienvenida("Andres")#Llama a la función con el nombre "Andres"s



def cuadrado(un_numero):#Calcula el cuadrado de un número
    return un_numero**2# Retorna el resultado

valor=cuadrado(5)#Imprime el valor retornado por la función
print(valor)#25


def multiplcar(num1,num2):#Función que multiplica dos números
    return num1*num2#Retorna el producto de dos números

resultado=multiplcar(5,2)#Llama a la función con los números 5 y 2
print(resultado)#10

