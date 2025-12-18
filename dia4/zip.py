nombres=['Camilo', 'Ana', 'Juan', 'Pedro'] #lista de nombres
edades=[25,30,22,28] #lista de edades
ciudades=['Bogota', 'Madrid', 'Mexico', 'Lima'] #lista de ciudades
combinados= list(zip(nombres,edades,ciudades)) #combinar las tres listas en una sola usando zip 
print(combinados) #imprimir el objeto zip 
print("-------------------")
for nombres,edades,ciudades in combinados: #iterar sobre cada tupla en el objeto zip
    print(f"{nombres} tiene {edades} años y vive en {ciudades}") #imprimir el nombre, edad y ciudad de cada persona