#Crea una función llamada devolver_distintos() que reciba 3
#integers como parámetros

def  devolver_distintos(num1,num2,num3):
    suma= num1+num2+num3
    if suma>15:
        return  max(num1,num2,num3)
    elif suma<10:
        return min(num1,num2,num3)
    elif suma>=10 and suma<=15:
        numeros_ordenados = sorted([num1,num2,num3]) #Ordena los números en orden ascendente
        numero_intermedio = numeros_ordenados[1] #Selecciona el número del medio
        return numero_intermedio

print(devolver_distintos(3,4,5)) #4
print(devolver_distintos(1,2,3)) #1
print(devolver_distintos(5,6,7)) #6