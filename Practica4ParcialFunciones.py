def holaMundo():
    print("Hola Mundo")
holaMundo()

def holaYoSoy(nombre):
    return "Hola yo soy{}".format(nombre)
hola=holaYoSoy(" Christian")
print(hola)

def suma(num1,num2,num3):
    return num1+num2+num3
print(suma(1,2,3))

def obtenerCurso():
    return "Curso","Python",3.0,"Celula","Cortazar"
print (obtenerCurso())
curso,lenguaje,version,* espacio= obtenerCurso()
print(espacio, lenguaje, version, curso)

def crearUsuario(nombre='', apellido='',edad=10):
     return{
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad
        }
usuario=crearUsuario("Franchesco",edad=16)
print(usuario)

def calcular(argumento_requerido, *args):
    print(argumento_requerido)
    total=0
    for aux in args:
        total+=aux
    return total
print(calcular(1,2,3,4,5,6,7,8,9))

def getUsuario(**kwargs):#Know Arguments genera diccionario (key values)
    print(kwargs)
getUsuario(nombre='Ana',apellido='Laguerfanita')


#Combinacion
def combinacion(argumento, *args, **kwargs):
    print(argumento)
    print(args)
    print(kwargs)
combinacion("Hola Mundo", 2,3,4,5,1,1,2, mensaje="Holaaa",id=20)

animal="Leon"#Variable global
def mostrarAnimal():
    animal="Tiburon"#Variable local
    print(animal)
mostrarAnimal()
print(animal)

animal="Leon"#Variable global
def mostrarAnimal():
    global animal
    animal="Tiburon"#Variable local
    print(animal)
mostrarAnimal()
print(animal)

#Funciones Lambda ahorras lineas especificando la funcion
farenheitCentigrados = lambda grados=0: (grados-32)/1.8
print(farenheitCentigrados(32))

