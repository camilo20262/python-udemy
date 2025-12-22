mi_archivo = open('prueba.txt','w') #abrir el archivo en modo escritura
mi_archivo.write("Hola como estas?")# sobre escribir en el archivo
mi_archivo.close() #cerrar el archivo


mi_archivo2 = open('prueba1.txt','w')# abrir el archivo en modo escritura
mi_archivo2.write("""Primera linea 
segunda linea
                  tercera linea""") #escribir primera linea
mi_archivo2.close() #cerrar el archivo

mi_archivo3 = open('prueba.txt','a') #abrir el archivo en modo agregar
mi_archivo3.write('\n yo estoy muy bien') #agregar una nueva linea al final del archivo
mi_archivo3.close() #cerrar el archivo