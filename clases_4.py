#Metodos estaticos
class Triangulo:
    numero = 2
    @staticmethod
    def area(base, altura):
        return (base*altura)//Triangulo.numero

isoceles = Triangulo()

print("el area es", Triangulo.area(10,20))