def abrir_leer(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

texto= abrir_leer('prueba.txt')
print(texto)
