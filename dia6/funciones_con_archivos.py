def abrir_leer(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

texto= abrir_leer('prueba.txt')
print(texto)


print("-----")

def sobrescribir(ruta):
    archivo= open(ruta,'w')
    contenido= archivo.write("contenido eliminado")
    archivo.close()
    return contenido
sobrescribir('prueba1.txt')
print(abrir_leer('prueba1.txt'))