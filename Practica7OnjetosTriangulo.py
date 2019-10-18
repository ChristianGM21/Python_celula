class Triangulo:
    area=10
    def _init_(self):
        self.area=0
    def calcularArea(self,base,altura):
        self.area=base*altura/2
    def getArea(self):
        return self.area

triangulo =Triangulo()
print(triangulo.area)
print(triangulo.getArea())
triangulo.calcularArea(10,20)
print(triangulo.getArea())
print(triangulo.area)
