class Triangulo:
    numero=2
    @staticmethod
    def area(base,altura):
        return base*altura/Triangulo.numero

    @classmethod
    def areaClase(cls,base,altura):
        return base*altura/cls.numero
print(Triangulo.area(10,100))
print(Triangulo.areaClase(10,200))
