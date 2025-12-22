mi_archivo = open('prueba.txt','w') #abrir el archivo en modo escritura
mi_archivo.write("Hola como estas?")# sobre escribir en el archivo
mi_archivo.close() #cerrar el archivo


mi_archivo2 = open('prueba1.txt','w')
mi_archivo2.write("""Primera linea
segunda linea
                  tercera linea""") #escribir primera linea
mi_archivo.close() #cerrar el archivo