#mi_archivo= open('prueba.txt') #abrir el archivo en modo lectura por defecto
#contenido= mi_archivo.read() #leer todo el contenido del archivo
#print(contenido) #imprimir el contenido en la consola
#mi_archivo.close() #cerrar el archivo

mi_archivo = open("prueba.txt", encoding="utf-8")

primera_linea = mi_archivo.readline()  # leer la primera línea
print(primera_linea)
segunda_linea = mi_archivo.readline() # leer la segunda línea
print(segunda_linea)

mi_archivo.close()



