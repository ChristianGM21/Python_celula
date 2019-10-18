pokemon={
    "nombre":"Charmander",
    "tipo":"Fuego",
    "ataque":"Ataque Solar"
    }
print(pokemon["nombre"])
print(pokemon.get("tipo"))
print(pokemon.get("evolucion"))
print(pokemon)
print(pokemon.get("evolucion","No existe perro"))
print(pokemon)
pokemon.setdefault("evolucion","Charmaleon")
print(pokemon)
print(pokemon.keys())
print(list(pokemon.keys()))
print(tuple(pokemon.values()))
print(pokemon.items())
#del pokemon["evolucion"]#limpia diccionario
valor=pokemon.pop("evolucion")#saca elementos
pokemon={}
pokemon.clear()
