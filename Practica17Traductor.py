#Christian Manuel González Mancera
#Practica No°17:Traductor
idiomas=(["1.Español"],["2.Ingles"],["3.Frances"])
print("Origen")
print(idiomas[0])
print(idiomas[1])
print(idiomas[2])
print("Destino")
print(idiomas[0])
print(idiomas[1])
print(idiomas[2])
origen=input("Introduce un origen")
lista = (["1.Hola","2.Adios","3.Comer","4.Correr","5.Alto","6.Bajo","7.Jugar","8.Perro","9.Gato","10.Bailar"],["1.Hello", "2.Goodbye", "3.Eat", "4.Run", "5.High", "6.Low", "7.Play", "8.Dog", "9.Cat", "10.Dance"],["1.Bonjour", "2.Au revoir", "3.Manger", "4.Courir", "5.Haut", "6.Bas", "7.Jouer", "8.Chien", "9.Chat", "10.Danse"])
while True:
    if(origen=="Español"):
        print("Esta es nuestra lista de palabras:",lista[0])
        destino=input("Introduce a que idioma deseas traducir")
        if(destino=="Ingles"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[1][0])
            elif(n==2):
                print(lista[1][1])
            elif(n==3):
                print(lista[1][2])
            elif(n==4):
                print(lista[1][3])
            elif(n==5):
                print(lista[1][4])
            elif(n==6):
                print(lista[1][5])
            elif(n==7):
                print(lista[1][6])
            elif(n==8):
                print(lista[1][7])
            elif(n==9):
                print(lista[1][8])
            elif(n==10):
                print(lista[1][9])
        elif(destino=="Frances"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[2][0])
            elif(n==2):
                print(lista[2][1])
            elif(n==3):
                print(lista[2][2])
            elif(n==4):
                print(lista[2][3])
            elif(n==5):
                print(lista[2][4])
            elif(n==6):
                print(lista[2][5])
            elif(n==7):
                print(lista[2][6])
            elif(n==8):
                print(lista[2][7])
            elif(n==9):
               print(lista[2][8])
            elif(n==10):
                print(lista[2][9])
        
    elif(origen=="Ingles"):
        print("Esta es nuestra lista de palabras:",lista[1])
        destino=input("Introduce a que idioma deseas traducir")
        if(destino=="Español"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[0][0])
            elif(n==2):
                print(lista[0][1])
            elif(n==3):
                print(lista[0][2])
            elif(n==4):
                print(lista[0][3])
            elif(n==5):
                print(lista[0][4])
            elif(n==6):
                print(lista[0][5])
            elif(n==7):
                print(lista[0][6])
            elif(n==8):
                print(lista[0][7])
            elif(n==9):
                print(lista[0][8])
            elif(n==10):
                print(lista[0][9])
        elif(destino=="Frances"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[2][0])
            elif(n==2):
                print(lista[2][1])
            elif(n==3):
                print(lista[2][2])
            elif(n==4):
                print(lista[2][3])
            elif(n==5):
                print(lista[2][4])
            elif(n==6):
                print(lista[2][5])
            elif(n==7):
                print(lista[2][6])
            elif(n==8):
                print(lista[2][7])
            elif(n==9):
                print(lista[2][8])
            elif(n==10):
                print(lista[2][9])
              
    elif(origen=="Frances"):
        print("Esta es nuestra lista de palabras:",lista[2])
        destino=input("Introduce a que idioma deseas traducir")
        if(destino=="Español"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[0][0])
            elif(n==2):
                print(lista[0][1])
            elif(n==3):
                print(lista[0][2])
            elif(n==4):
                print(lista[0][3])
            elif(n==5):
                print(lista[0][4])
            elif(n==6):
                print(lista[0][5])
            elif(n==7):
                print(lista[0][6])
            elif(n==8):
                print(lista[0][7])
            elif(n==9):
                print(lista[0][8])
            elif(n==10):
                print(lista[0][9])
        elif(destino=="Inges"):
            n=int(input("Introduce el numero de la palabra que deseas traducir"))
            if(n==1):
                print(lista[1][0])
            elif(n==2):
                print(lista[1][1])
            elif(n==3):
                print(lista[1][2])
            elif(n==4):
                print(lista[1][3])
            elif(n==5):
                print(lista[1][4])
            elif(n==6):
                print(lista[1][5])
            elif(n==7):
                print(lista[1][6])
            elif(n==8):
                print(lista[1][7])
            elif(n==9):
                print(lista[1][8])
            elif(n==10):
                print(lista[1][9])
    iniciar=input("Desea continuar ponga 1 si desea terminar ponga 2")
    if iniciar==1:
        break
print ("fin del programa")


