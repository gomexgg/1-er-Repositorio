#Práctica 8
#Jesús Gómez Guijarro
#Polimorfismo
class Perro:
    def hacer_sonido(self):
        return "Guau Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau Miau"

class Vaca:
    def hacer_sonido(self):
        return "Muuu"

# Función que usa polimorfismo
def hacer_sonar(animal):
    print(animal.hacer_sonido())  

# Uso
perro = Perro()
gato = Gato()
vaca = Vaca()

hacer_sonar(perro)  
hacer_sonar(gato)   
hacer_sonar(vaca)   