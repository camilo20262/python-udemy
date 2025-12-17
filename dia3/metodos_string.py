texto= "esto es un texto de preuba para probar funciones de strings"
prueba = texto.upper() # Convierte todo a mayusculas
print(prueba)
prueba = texto.lower() # Convierte todo a minusculas
print(prueba)

prueba = texto.lower().capitalize() # Convierte la primera letra en mayuscula
print(prueba)

prueba = texto.title() # Convierte la primera letra de cada palabra en mayuscula
print(prueba)

prueba = texto.split() # Convierte el texto en una lista de palabras
print(prueba)

texto2= "esto-es-un-texto-de-preuba-para-probar-funciones-de-strings"
prueba2= texto2.split("-") # Convierte el texto en una lista de palabras usando un separador
print(prueba2)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e="".join([a,b,c,d]) # Une una lista de palabras en un solo texto sin espacios
print(e)



texto= "esto es un texto de preuba para probar funciones de strings"
cambiar = texto.replace("texto", "fragmento") # Reemplaza una palabra por otra
print(cambiar)
cambiar = texto.replace(" ", "_") # Reemplaza los espacios por guiones bajos
print(cambiar)

