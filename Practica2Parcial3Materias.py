#Promedios
calificaciones={}
materias=("Base de Datos","Redes","Programacion","Moviles")
mayor=0
promedio=0
for materia in materias:
    valor=float(input("¿Que calificacion tienes en la materia"+materia+"?"))
    calificaciones.setdefault(materia,valor)
    print(calificaciones)
    lista=tuple(calificaciones.values())

for indice,calificacion in enumerate(lista):
    mayor=int(indice if calificacion>list(calificaciones.values())[mayor]else mayor)
    promedio+=calificacion

print("La calificacion con mayor promedio fue:"+materias[mayor])
print("Tu promedio general fue de:"+str(promedio/len(materias)))
    
