#Práctica 13
#Jesús Gómez Guijarro
#Arreglos, Listas, Conjuntos y Diccionarios
# Diccionarios
dic = {"x": "equis", "y": "ye", "z": "zeta"}
print(dic)
dic = dict(x="equis", y="ye", z="zeta")
print(dic)
print(dic["x"])
print(dic.get("x"))
print(dic.get("a"))

dic["x"] = "equisD"
print(dic)
dic["a"] = "a"
print(dic)
del dic["a"]
print(dic)
x = dic.pop("x")
print(x)
print("y" in dic)
print(dic.values())
p = dic.items()
print(p)
print(dic.keys())
print(dic.update({"x": "equis"}))
print(dic.clear())