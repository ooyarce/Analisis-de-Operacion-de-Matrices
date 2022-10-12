Estos son códigos python que estudian el rendimiento de dos algoritmos distintos de operaciones matriciales. 

En python, las funciones numpy.linalg.inv  y scipy.linalg.inv ambas calculan la inversa multiplicativa de matrices. Siguiendo el formato anterior, determine el desempeño de ambas funciones para tamaños crecientes de matrices. Además, determine si en su sistema utilizar la opción overwrite_a=True de scipy.linalg.inv resulta en ganancia de desempeño. 

Determine los tamaños en memoria de cada uno de estos tipos de datosEnlaces a un sitio externo. en python para su sistema (cada sistema puede variar):

-np.half

-np.single

-np.double

-np.longdouble

Para los tipos de datos que sean distintos en su sistema, determine la eficiencia en los siguientes casos:

-Para numpy.linalg.inv

-Para la función scipy.linalg.inv con overwrite_a=False

-Para la función scipy.linalg.inv con '''overwrite_a=True''' considerando el uso de memoria exigida por cada tipo de dato, para una matriz Laplaciana de la siguientes formas:


Monitorée el uso de memoria y procesadores en cada caso y comente lo que ve a la luz de lo discutido en la clase del 10 de Agosto de 2020. Nombre cada script python de la siguiente manera timing_inv_caso_X_dtype.py. Por ejemplo, el caso 2 usando tipo de datos longdouble sería llamado timing_inv_caso_2_longdouble.py.
