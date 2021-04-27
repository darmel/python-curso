#Clase Object
#declaracion de clase
class Perro:
    def __init__(self,nombre):
        self.nombre = nombre

class Pajarito(object): #estoy heredando todo de la clase object
    def __init__(self,nombre):
        self.nombre = nombre

perrito = Perro("Toby")
cardenal = Pajarito("pepito")

print(perrito.__init__)