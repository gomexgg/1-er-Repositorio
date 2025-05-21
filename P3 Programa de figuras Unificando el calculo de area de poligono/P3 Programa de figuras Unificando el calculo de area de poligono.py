#Práctica 3
#Jesús Gómez Guijarro
#Programa de figuras Unificando el calculo de area de poligono
from math import pi, tan

class Poligono:
    
    def calcular_area(longitud_lado, cantidad_lados):
        area = (1 / 4) * cantidad_lados * (longitud_lado ** 2) / tan(pi / cantidad_lados)
        return area

    def calcular_perimetro(longitud_lado, cantidad_lados):
        perimetro = longitud_lado * cantidad_lados
        return perimetro

cantidad_lados = int(input("Ingrese el número de lados del polígono: "))
longitud_lado = float(input("Ingrese la longitud de un lado: "))

if cantidad_lados <= 2 or longitud_lado <= 0:
    print("El polígono no es válido.")
else:
    print(f"El área del polígono es: {Poligono.calcular_area(longitud_lado, cantidad_lados)}")
    print(f"El perímetro del polígono es: {Poligono.calcular_perimetro(longitud_lado, cantidad_lados)}")