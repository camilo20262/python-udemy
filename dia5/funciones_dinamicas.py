def chequear_3_cifras(lista): 
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado = chequear_3_cifras ([555,99,600])
print(resultado)

def todos_positivos(lista_numeros): #Función que verifica si todos los números en una lista son positivos
    for n in lista_numeros: #Itera sobre cada número en la lista
        if n < 0: #Si encuentra un número negativo
            return False 
    return True

print(todos_positivos([1,2,3,4,-5]))  # False
print(todos_positivos([1,2,3,4,5]))   # True
