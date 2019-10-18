class Animal:
    def comer(self):
        print("Comer")
    def dormir(self):
        print("Dormir")
class Perro(Animal):
    def ladrar(self):
        print("Woff!")
class Gato(Animal):
    def ronronear(self):
        print("Miaww!")

gato=Gato()
perro=Perro()
toro=Animal()
gato.ronronear()
gato.dormir()
print()
perro.ladrar()
perro.comer()
print()
toro.dormir()
toro.comer()
#toro.ronronear()
        
