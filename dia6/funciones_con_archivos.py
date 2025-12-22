def abrir_leer(ruta): #función para abrir y leer un archivo
    archivo = open(ruta, 'r') #abrir el archivo en modo lectura
    contenido = archivo.read() #leer el contenido del archivo 
    archivo.close()#cerrar el archivo 
    return contenido#retornar el contenido leído

texto= abrir_leer('prueba.txt') #llamar a la función para abrir y leer el archivo prueba.txt
print(texto) #imprimir el contenido leído


print("-----")

def sobrescribir(ruta):#función para sobrescribir el contenido de un archivo
    archivo= open(ruta,'w') #abrir el archivo en modo escritura
    contenido= archivo.write("contenido eliminado") #sobrescribir el contenido del archivo
    archivo.close() #cerrar el archivo
    return contenido #retornar el contenido sobrescrito
sobrescribir('prueba1.txt') #llamar a la función para sobrescribir el archivo prueba1.txt
print(abrir_leer('prueba1.txt')) #leer y mostrar el contenido del archivo prueba1.txt después de sobrescribirlo


print("-----")

def registro_error(ruta):
    archivo = open(ruta,'a')
    contenido = archivo.write("\nse ha registrado un error de ejecución")
    archivo.close()
    return contenido

registro_error('prueba1.txt')
print(abrir_leer('prueba1.txt'))
    
