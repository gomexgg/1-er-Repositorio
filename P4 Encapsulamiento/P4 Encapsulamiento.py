#Práctica 4
#Jesús Gómez Guijarro
#Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado
    
 
    def consultar_saldo(self):
        return f"El saldo actual de {self.__titular} es: ${self.__saldo:.2f}"
    
    # Método para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.__saldo:.2f}"
        else:
            return "El monto a depositar debe ser mayor a 0."
    
    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            return "Fondos insuficientes para realizar el retiro."
        elif cantidad > 0:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}"
        else:
            return "El monto a retirar debe ser mayor a 0."

# Crear una instancia de CuentaBancaria
mi_cuenta = CuentaBancaria("Fulanito", 1000.0)

# Simular operaciones bancarias
print(mi_cuenta.consultar_saldo())  # Consultar saldo
print(mi_cuenta.depositar(500))    # Depositar dinero
print(mi_cuenta.retirar(200))      # Retirar dinero
print(mi_cuenta.retirar(2000))     # Intentar retirar más del saldo