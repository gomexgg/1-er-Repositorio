#Práctica 9
#Jesús Gómez Guijarro
#ENUM
from enum import Enum
class Consecutive(Enum):
    Lunes=1
    Martes=2
    Miercoles=3
    Jueves=4
    Viernes=5

print(Consecutive.Lunes) 

print(Consecutive.Lunes.value)

print(type(Consecutive.Lunes))

print(type(Consecutive.Lunes.value))