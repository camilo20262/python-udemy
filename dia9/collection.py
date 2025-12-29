from collections import Counter, defaultdict, namedtuple


numeros = [1,2,5,4,5,6,8,7,8,5,6,2,3,1,4,2,5,8,9,7,4,23,6] # lista de numeros 

print(Counter(numeros)) # contar cuantas veces se repite en la lista 
print('------')
frase ="al pan pan y al vino vino"
print(Counter(frase.split()))
print('------')
mi_dic= defaultdict(lambda:'Nada')
print('------')
mi_dic['Uno']= 'Verde'
print(mi_dic['Dos'])
print('------')
print(mi_dic)

print('------')

persona= namedtuple('Persona',['nombre','altura','peso'])
ariel= persona('camilo',1.80,75)
print(ariel.peso)