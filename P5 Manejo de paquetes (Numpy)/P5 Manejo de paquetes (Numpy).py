#Práctica 5
#Jesús Gómez Guijarro
#Manejo de paquetes (Numpy)

from numpy import array
import numpy as np

class OperacionesNumpy:
    
    def __init__(self, valores):
        self.arreglo = np.array(valores)

    def agregar_elemento(self, valor):
        self.arreglo = np.insert(self.arreglo, indice, valor)
        print(self.arreglo)

    def quitar_elemento(self, indice):
        self.arreglo = np.delete(self.arreglo, indice)
        print(self.arreglo)

    def actualizar_elemento(self, indice, nuevo_valor):
        self.arreglo[indice] = nuevo_valor
        print(self.arreglo)


class OperacionesLista:
    
    def __init__(self, valores):
        self.lista = []

    def agregar(self, valor):
        self.lista.append(valor)
        print(self.lista)

    def quitar(self, indice):
        self.lista.pop(indice)
        print(self.lista)

    def actualizar(self, indice, nuevo_valor):
        self.lista[indice] = nuevo_valor
        print(self.lista)


# Valores iniciales
valor_inicial = 7
indice = 0
nuevo_valor = 8

# Trabajando con Numpy
print("Operaciones con Numpy-------------------")
operaciones_np = OperacionesNumpy(valor_inicial)

operaciones_np.agregar_elemento(3)
operaciones_np.agregar_elemento(6)
operaciones_np.agregar_elemento(9)

operaciones_np.actualizar_elemento(2, 5)
print("Remover elemento")
operaciones_np.quitar_elemento(0)

# Trabajando con Listas
print("Operaciones con Listas-------------------")
operaciones_lista = OperacionesLista(valor_inicial)
operaciones_lista.agregar(11)
operaciones_lista.agregar(12)
operaciones_lista.agregar(13)
operaciones_lista.agregar(14)
operaciones_lista.quitar(1)
operaciones_lista.actualizar(1, 20)