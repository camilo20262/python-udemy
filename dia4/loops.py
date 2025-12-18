lista = ['a', 'b', 'c', 'd', 'e'] #lista de letras
for letra in lista: #iterar sobre cada letra en la lista
    posicion = lista.index(letra) +1 #obtener la posicion de la letra en la lista (sumando 1 para empezar desde 1)
    print(f"letra es : {letra} en la posicion {posicion}") #imprimir la letra y su posicion
