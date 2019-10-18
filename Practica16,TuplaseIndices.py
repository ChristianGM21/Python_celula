tupla = ("Java","Python","C++","PHP","JavaScript","Dart")
lista = ["Java","Python","C++","PHP","JavaScript","Dart"]
#Ordenar
lista.sort()

print(tupla)
print(lista)

lista.sort(reverse=True)
print(lista)

#Max-Min
print(min(tupla))
print(max(lista))

#Longitud
print(len(tupla))
print(len(lista))

#in
print("Python" in tupla)
print("Ruby" in lista)

#indices
print(lista.index("Python"))

#count
print(lista.count("Python"))
print(tupla.count("C"))
