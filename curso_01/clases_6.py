#Herencia

class Cuadrupedos:
    patas: 4
    ojos: 2
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print(self.nombre, "esta comiendo de cuadrupedo")
    def dormir(self):
        print(self.nombre, "esta durmiendo")

class Mascota:
    def direccion(self, dire):
        self.dire = dire
        print(self.nombre, "vive en", dire)
    def comer(self):
        print(self.nombre, "esta comiendo com,ida de mascota")


#la clase Gato va a tener lo de gato y va a heredar todo lo de Cuadrupedos
#class Gato(Cuadrupedos):
#    def maullar(self):
#        print(self.nombre, "maullando")

#la clase Gato va heredar todo lo de Cuadrupedos y además los metodos de Mascota
class Gato(Cuadrupedos, Mascota):
    def maullar(self):
        print(self.nombre, "maullando")
    #def comer(self):
    #       print(self.nombre, "esta comiendo de gato")

#gandalf = Cuadrupedos("gandalf")

gandalf = Gato("Gandalf") 
gandalf.comer()
gandalf.maullar()
gandalf.direccion("tacuari 542")

#el metodo que vale es el de la clase final por sobre los otros
#si no esta en la clase final busca en las primeras heredadas, marcadas en la definicion de la clase
gandalf.comer()