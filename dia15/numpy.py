# Importamos Numpy con su abreviación "np"
import numpy as np 
# Podemos crear arrays de una dimensión con la función np.array()
array_unids= np.array([1,2,3,4,5])


# O un array de dos dimensiones (bidimensional)

array_bidi= np.array([[1,2,3],
                      [4,5,6]])


# O un array de tres dimensiones (tridimensional)
array_tridi= np.array([[[1,2,3],
                        [4,5,6]],
                       [[7,8,9],
                        [10,11,12]]])

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
array_unids.shape,array_unids.ndim, array_unids.dtype,array_unids.size,type(array_unids)

# Atributos del array bidimensional
array_bidi.shape,array_bidi.ndim, array_bidi.dtype,array_bidi.size,type(array_bidi)

# Atributos del array tridimensional
array_tridi.shape,array_tridi.ndim, array_tridi.dtype,array_tridi.size,type(array_tridi)

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional

import pandas as pd 
datos= pd.DataFrame(array_bidi)
datos

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)

unos= np.ones((4,3))
unos


# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)

zero= np.zeros((2,4,3))
zero    


# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0,101,5)
array_1


# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0,10,(2,5))
array_2



# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)
array_3 = np.random.random((3,5))
array_3
# Establecemos la "semilla" de números aleatorios en 27


# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_4 = np.random.randint(0,10,(5,8))
array_4


# Encontramos los valores únicos del array_4
np.unique(array_4)

# Extraemos el elemento de índice 1 del array_4
array_4[1]

# Extraemos los dos primeros datos de las primeras dos filas del array_4
array_4[:2,:2]

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
array_5= np.random.randint(0,10,(3,4))
array_6=np.ones((3,4))

# Sumamos los dos arrays

array_5 +array_6


# Creamos ahora un array de tamaño (4,3) lleno de unos
array_7 = np.ones((4,3))


# Intentaremos sumar los arrays 6 y 7
array_6 + array_7  # Esto nos dará un error, ya que las dimensiones no son compatibles para la suma


# Entonces crearemos otro array de tamaño (4,3) lleno de unos
array_8 = np.ones((4,3))

# Restamos el array_8 al array_7
array_8 - array_7


# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
array_9= np.random.randint(1,5,(3,3))
array_10= np.random.randint(1,5,(3,3))


# Multiplicamos los últimos dos arrays entre sí

array_9* array_10

# Elevamos el array_9 al cuadrado

array_9 **2

# Buscamos la raíz cuadrada del array_10

np.sqrt(array_10)


# Hallamos el promedio de los valores del array_9
array_9.mean()

# Hallamos el valor máximo de los valores del array_9
array_9.max()

# Hallamos el valor mínimo de los valores del array_9
array_9.min()

# Cambiamos la forma del array_9 por una de 9x1, y lo almacenamos como array_11
array_11= array_9.reshape(9,1)

# Comparamos el array_9 y el array_10, para saber cuáles elementos del array_9 son mayores a los del array_10

array_12 = array_9 > array_10
array_12

# Veamos sus nuevos tipos de datos
array_12.dtype