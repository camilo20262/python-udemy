dic1={ 'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
print(dic1)
valor= dic1['c2'] # Accede al valor de la clave 'c2'
print(valor)



cliente = {'nombre': 'Juan', 'apellido': 'Fuentes','peso':88, 'talla':1.75}
consulta = (cliente ['apellido']) # Accede al valor de la clave 'apellido'
print(consulta)

cliente["pais"]="Colombia" # Agrega una nueva clave 'pais' con su valor
print(cliente)

cliente["peso"]=85 # Modifica el valor de la clave 'peso'
print(cliente)

del cliente["talla"] # Elimina la clave 'talla' y su valor
print(cliente)