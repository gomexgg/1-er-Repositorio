#Práctica 13
#Jesús Gómez Guijarro
#Arreglos, Listas, Conjuntos y Diccionarios
# Conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
# Unión
union = a.union(b)
print("Unión:", union)
# Intersección
interseccion = a.intersection(b)
print("Intersección:", interseccion)
# Diferencia
diferencia = a.difference(b)
print("Diferencia:", diferencia)
diferenciaMenos = b-a
print("Diferencia menos:", diferenciaMenos)
# Diferencia simétrica
diferenciaSimetrica = a.symmetric_difference(b)
print("Diferencia simétrica:", diferenciaSimetrica)
diferenciaExpresion = a ^ b
print("Diferencia simétrica expresion:", diferenciaExpresion)
# Subconjunto
a = {1,2,3}
b = {1,2,3,4,5}
c = {}
print(type(c))
subconjunto = a.issubset(b)
print("Subconjunto:", subconjunto)
# Superconjunto
superconjunto = b.issuperset(a)
print("Superconjunto:", superconjunto)
# Disjunto
a= {1, 2, 3}
b= {4, 5, 6}
disjunto = a.isdisjoint(b)
print("Disjunto:", disjunto)
#copia
a = {1, 2, 3}
e = a.copy()
print("Copia de a:", e)

al = len(a)
print("Longitud de a:", al)
print(a.clear())