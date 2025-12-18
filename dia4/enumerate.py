lista= ['a', 'b', 'c', 'd', 'e'] #lista de letras
for indice, letra in enumerate(lista): #iterar sobre cada letra en la lista con su indice
    print(indice,letra) #imprimir el indice y la letra



print("-------------------")
tupla=list(enumerate(lista))#crear una tupla de indices y letras usando enumerate
print(tupla) #imprimir la tupla de indices y letras
print(tupla[2][0]) #imprimir el indice del tercer elemento


print("-------------------")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice, nombre)