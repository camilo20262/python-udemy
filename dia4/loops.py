lista = ['a', 'b', 'c', 'd', 'e'] #lista de letras
for letra in lista: #iterar sobre cada letra en la lista
    posicion = lista.index(letra) +1 #obtener la posicion de la letra en la lista (sumando 1 para empezar desde 1)
    print(f"letra es : {letra} en la posicion {posicion}") #imprimir la letra y su posicion



lista1= ["camilo", "ana", "juan", "pedro"] #lista de nombres
for nombre in lista1: #iterar sobre cada nombre en la lista
    if nombre.startswith("a"): #verificar si el nombre empieza con la letra "a"
        print(f"{nombre} empieza con la letra a")   #imprimir que el nombre empieza con "a"
    else:
        print(f"{nombre} no empieza con la letra a") #imprimir que el nombre no empieza con "a"