#Enumerate
#lista=[1,2,3,4,5]
#for indice,valor in enumerate(lista):
 #   print("Indice:",indice,"Valor:",valor)

#texto="Hola Mundo"
#for letra in texto:
    #if letra=="M":
     #break
    #print(letra)

#texto="Hola Mundo"
#for letra in texto:
 #   if letra=="M":
  #   continue
   # print(letra)


calificacion=90.5
color=""
if calificacion>=60:
    color="Verde"
    print(color)
else:
    color="Rojo"
    print(color)

color="Verde" if calificacion>=60 else "Rojo"
print(color)
