
from operator import inv
import re


def saludar_persona(nombre):#Función que saluda a una persona por su nombre
    print("Hola, como estas? "+nombre)#Imprime el saludo

saludar_persona("Camila")#Llama a la función con el nombre "Camila"
print("-----")
def bienvenida(nombre_persona):#Función que da la bienvenida a una persona
    print(f"¡Bienvenido {nombre_persona}!")#Imprime el mensaje de bienvenida
bienvenida("Andres")#Llama a la función con el nombre "Andres"s



def cuadrado(un_numero):#Calcula el cuadrado de un número
    return un_numero**2# Retorna el resultado
print("-----")
valor=cuadrado(5)#Imprime el valor retornado por la función
print(valor)#25

print("-----")
def multiplcar(num1,num2):#Función que multiplica dos números
    return num1*num2#Retorna el producto de dos números

resultado=multiplcar(5,2)#Llama a la función con los números 5 y 2
print(resultado)#10

print("-----")
def invertir_palabra(palabra):#Función que invierte una palabra y la convierte a mayúsculas
    invertido = palabra[::-1].upper()# Invierte la palabra y la convierte a mayúsculas
    return invertido #Retorna la palabra invertida y en mayúsculas

palabra=invertir_palabra("python") #Llama a la función con la palabra "python"
print(palabra)#NOHTYP 
print(invertir_palabra("camilo"))#OLIMAC
