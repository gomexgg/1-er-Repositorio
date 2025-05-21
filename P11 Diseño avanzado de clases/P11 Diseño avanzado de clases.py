#Práctica 11
#Jesús Gómez Guijarro
#Diseño avanzado de clases
# Encapsulamiento
class Patron:
    def traerCheve(self):
        pass

class Morra:
    def traerCheve(self):
        return "Yo sí traigo y pago cheves por ser buchona empoderada."

class Pisto: 
    def __init__(self, hielera, hielera2):
        self.__hielera = hielera  # Atributo privado
        self.hielera2 = hielera2  # Atributo público

    def pistear(self):
        self.__hielera = "vaciar"
        return self.__hielera
    
    def pistear2(self):
        self.hielera2 = "Está vacía"
        return self.hielera2

# Crear una instancia de Pisto
fiesta = Pisto("Cartón en hielera", "Unas cuantas frías")
print(fiesta.pistear())
print(fiesta.pistear2())