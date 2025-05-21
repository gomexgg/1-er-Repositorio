#Práctica 2
#Jesús Gómez Guijarro
#Programa de figuras CON PARAMETROS


class Cuadrado:
    # Método para calcular el perímetro
    def perimetro(self, lado):
        p = lado * 4  # Fórmula para calcular el perímetro
        return p

    # Método para calcular el área
    def area(self, lado):
        a = lado ** 2  # Fórmula para calcular el área
        return a

# Crear una instancia de la clase
cuadrado = Cuadrado()

# Llamar a los métodos pasando el valor como parámetro
lado = 4
print(f"Perímetro: {cuadrado.perimetro(lado)}")  # Salida: Perímetro: 16
print(f"Área: {cuadrado.area(lado)}")           # Salida: Área: 16