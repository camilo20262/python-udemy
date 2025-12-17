mi_lista=["a","b","c","d","e"]
print(mi_lista)
resultado= len(mi_lista) # Devuelve la cantidad de elementos en la lista
print(resultado)
print(mi_lista[0]) # Accede al primer elemento de la lista
print(mi_lista[-1]) # Accede al ultimo elemento de la lista
print(mi_lista[1:4]) # Accede a una porcion de la lista desde el indice 1 hasta el 3
mi_lista2=["f","g","h","i","j"]
mi_lista3= mi_lista + mi_lista2 # Une dos listas
print(mi_lista3)
mi_lista3.append("k") # Agrega un elemento al final de la lista
print(mi_lista3)

mi_lista3.pop() # Elimina el ultimo elemento de la lista
print(mi_lista3)
mi_lista3.pop(0) # Elimina el elemento en el indice 0
print(mi_lista3)


lista = ['g','f','b','m','c']
lista.sort()
print(lista) # Ordena la lista en orden alfabetico
lista.reverse()
print(lista) # Invierte el orden de la lista
