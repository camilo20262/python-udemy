mi_archivo2= open('prueba.txt') #abrir el archivo en modo lectura por defecto
contenido= mi_archivo2.read() #leer todo el contenido del archivo
print(contenido) #imprimir el contenido en la consola
mi_archivo2.close() #cerrar el archivo
print("-----")
mi_archivo = open("prueba.txt", encoding="utf-8")

primera_linea = mi_archivo.readline()  # leer la primera línea
print(primera_linea)
segunda_linea = mi_archivo.readline() # leer la segunda línea
print(segunda_linea)

mi_archivo.close()


print("-----")
mi_archivo3 = open("prueba.txt", encoding="utf-8")
lineas = mi_archivo3.readlines()  # leer todas las líneas y guardarlas en una lista
print(lineas)# imprimir la lista de líneas
mi_archivo3.close() # #cerrar el archivo







