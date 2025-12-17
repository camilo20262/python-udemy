texto=input("Ingresee un texto :")
letra1=input("Ingrese la letra uno :")
letra2=input("Ingrese la letra dos :")
letra3=input("Ingrese la letra tres :")

cantidad=[letra1,letra2,letra3]
print("el texto es ",texto)
print("La cantidad de caracteres del texto es :",len(texto))
print("La cantidad de veces que aparece la letra",letra1," es :",texto.count(letra1))
print("La cantidad de veces que aparece la letra",letra2," es :",texto.count(letra2))
print("La cantidad de veces que aparece la letra",letra3," es :",texto.count(letra3))
print("La primera letra es:", texto[0])
print("La última letra es:", texto[-1])


al_reves=texto[::-1]
print("El texto al reves es :",al_reves)

print("python"in texto)



