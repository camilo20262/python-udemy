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