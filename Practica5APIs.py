import requests
def getInfo(url="https://pokeapi.co/api/v2/pokemon"):
    response = requests.get(url)
    if(response.status_code==200):
        return response.json()
    else:
        return "Error"
#print(getInfo())
    
def listarPokemon(pokemons):
    print("--------------------------------------------------------------------")
    for pokemon in pokemons:
        printPokemon(pokemon)
def printPokemon(pokemon):
    print("--------------------------------------------------------------------")
    print("\t Nombre: "+pokemon.get("name"))
    print("\t Imagen: "+pokemon.get("url"))

response = getInfo()
if(response != "Error"):
    for x in range(3):
        listarPokemon(list(response.get("results")))
        reponse=getInfo(response.get('next'))
else:
    print(response)
