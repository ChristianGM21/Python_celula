import requests
origen=input("Introduce una ciudad")
def getInfo(url="http://api.openweathermap.org/data/2.5/weather?q="+origen+"&mode=json&units=metric&lang=es&appid=2b9d7ab6c5f2e7946ea29ffcc5c956e5"):
    response = requests.get(url)
    if(response.status_code==200):
        return response.json()
    else:
        return "Error"

def listarClimas(climas):
    for clima in climas:
        printClima(clima)
        
def printClima(clima):
    print("\t Descripcion: "+clima.get("description"))
    print("--------------------------------------------")
response=getInfo()
if(response!="Error"):
        listarClimas(list(response.get("weather")))
else:
    print(response)
def printTiempo(tiempo):
    print("\t Temperatura: "+str(tiempo.get("temp")))
    print("--------------------------------------------")
    print("\t Humedad: "+str(tiempo.get("humidity")))
    print("--------------------------------------------")
    print("\t Temperatura-Minima: "+str(tiempo.get("temp_min")))
    print("--------------------------------------------")
    print("\t Temperatura-Maxima: "+str(tiempo.get("temp_max")))
    print("--------------------------------------------")
response=getInfo()
if(response!="Error"):
        printTiempo(response.get("main"))
else:
    print(response)


