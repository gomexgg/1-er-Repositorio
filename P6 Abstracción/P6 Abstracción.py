#Práctica 6
#Jesús Gómez Guijarro
#Abstracción

from abc import ABC, abstractmethod  # Importamos para hacer una clase abstracta

class Figura(ABC):  
    @abstractmethod
    def calcular_area(self):  
        pass  

class Cuadrado(Figura):  # Clase que hereda de Figura
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):  # Ahora sí implementamos el cálculo del área
        return self.lado * self.lado

class Circulo(Figura):  
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio

# Uso
cuadrado = Cuadrado(4)
circulo = Circulo(3)

print(cuadrado.calcular_area())  
print(circulo.calcular_area())   