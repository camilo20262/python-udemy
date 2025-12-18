from random import * #importar todo del modulo random

aleatorio1 = randint(1,100) #generar un numero aleatorio entre 1 y 100
print(aleatorio1) #print el numero aleatorio generado
print("--------------")
aleatorio2= round(uniform(1,10),2) #generar un numero aleatorio decimal entre 1 y 10
print(aleatorio2) #print el numero aleatorio generado
print("--------------")
aleatorio3=random() #generar un numero aleatorio entre 0 y 1
print(aleatorio3) #print el numero aleatorio generado

print("--------------")
aleatorio4= choice(['rojo', 'verde', 'azul', 'amarillo']) #elegir un elemento aleatorio de una lista
print(aleatorio4) #print el elemento aleatorio elegido