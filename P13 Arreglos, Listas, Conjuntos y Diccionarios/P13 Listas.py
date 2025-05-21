#Práctica 13
#Jesús Gómez Guijarro
#Arreglos, Listas, Conjuntos y Diccionarios
# Listas

import numpy as np

# Crear una lista de 5 valores mixtos (int y float)
lista_mixta = [10, 20.5, 30, 40.8, 50]

# Crear listas de 5 valores del mismo tipo (usando numpy y listas normales)
lista_numpy = np.array([1, 2, 3, 4, 5])  # Numpy array de enteros
lista_regular = [10, 20, 30, 40, 50]  # Lista común de enteros
lista_manual = list([100, 200, 300, 400, 500])  # Lista creada con el constructor `list`

# Convertir las listas anteriores a tuplas y conjuntos
tupla_numpy = tuple(lista_numpy)  # Convertir numpy array a tupla
conjunto_numpy = set(lista_numpy)  # Convertir numpy array a conjunto
conjunto_regular = set(lista_regular)  # Convertir lista regular a conjunto

# Crear un diccionario de 5 elementos con valores de distintos tipos
diccionario = {
    "entero": 100,
    "float": 3.14,
    "string": "Python",
    "booleano": True,
    "lista": [1, 2, 3]
}

# Imprimir resultados iniciales
print("Lista Mixta:", lista_mixta)
print("Lista con Numpy:", lista_numpy)
print("Lista Regular:", lista_regular)
print("Tupla (de Numpy):", tupla_numpy)
print("Conjunto (de Numpy):", conjunto_numpy)
print("Conjunto (de Lista Regular):", conjunto_regular)
print("Diccionario:", diccionario)

# Manipular la lista regular
lista_regular.append(99)  # Agregar un elemento al final
lista_regular.insert(1, 98)  # Insertar un elemento en la posición 1
lista_regular.extend([2, "hola"])  # Extender la lista con nuevos elementos


indice_30 = lista_regular.index(30)  
conteo_10 = lista_regular.count(10)  


print("\nLista Manipulada:")
print("Lista después de append, insert y extend:", lista_regular)
print("Índice del valor 30:", indice_30)
print("Conteo del valor 10:", conteo_10)

