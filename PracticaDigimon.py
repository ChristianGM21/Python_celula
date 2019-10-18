import requests

def getInfo(url="https://digimon-api.herokuapp.com/api/digimon"):

    response=requests.get(url)

    if(response.status_code==200):
        return response.json()
    else:
        return "Error"


def printDigimon(digimon):
    print("----------------------------------------------------------------------")
    print("\t Nombre: "+digimon.get("name"))
    print("\t Imagen: "+digimon.get("img"))
    print("\t Nivel: "+digimon.get("level"))

def listarDigimon(digimons):
    print("-----------------------------------------------------------------------")
    for digimon in digimons:
        printDigimon(digimon)

response=getInfo()
if(response!="Error"):
        listarDigimon(response)
else:
    print(response)
