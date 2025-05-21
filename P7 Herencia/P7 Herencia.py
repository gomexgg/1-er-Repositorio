#Práctica 7
#Jesús Gómez Guijarro
#Herencia
class Transporte:
    def __init__(self, fabricante, version):
        self.fabricante = fabricante
        self.version = version

    def mostrar_info(self):
        return self.fabricante + " " + self.version


class Automovil(Transporte):
    def __init__(self, fabricante, version, puertas):
        super().__init__(fabricante, version)  # Llama al constructor de la clase base
        self.puertas = puertas

    def mostrar_info(self):
        return "Automóvil: " + super().mostrar_info() + ", " + str(self.puertas) + " puertas"

# Otra clase derivada que hereda de Transporte
class Ciclo(Transporte):
    def __init__(self, fabricante, version, categoria):
        super().__init__(fabricante, version)  # Llama al constructor de la clase base
        self.categoria = categoria

    def mostrar_info(self):
        return "Ciclo: " + super().mostrar_info() + ", categoría " + self.categoria

# Uso de las clases
auto = Automovil("Honda", "Civic", 4)
bici = Ciclo("Specialized", "Rockhopper", "Deportiva")

print(auto.mostrar_info())  # Salida: Automóvil: Honda Civic, 4 puertas
print(bici.mostrar_info())  # Salida: Ciclo: Specialized Rockhopper, categoría Deportiva