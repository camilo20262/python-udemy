mascota= input("Que mascota tienes? ")
if mascota.lower() == "perro":
    print("Tienes un perro")
elif mascota.lower() =="gato":
    print("Tienes un gato")
elif mascota.lower()== "loro":
    print("Tienes un loro")
else:
    print("tienes un otro tipo de mascota")


edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')