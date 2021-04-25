#clases con variables de instancia vs de clase

class Gato:
    patas = 4 #variables de clase
    ojos = 2 
    def __init__(self, nombre):
        self.nombre = nombre #variable de instancia, 

gandalf = Gato("Gandalf")
tutu = Gato("tutusuaria")

print("los Gatos tienen", Gato.patas, "patas")
print(gandalf.nombre)
print(tutu.nombre)

print("el gato", gandalf.nombre, "tiene", gandalf.patas, "patas")

