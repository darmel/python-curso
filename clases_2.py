#clases atributos
#class (palabra reservada) El nombre de la clase comienza en mayuscula
#metodo init
class Persona: 
    #pass //pass es para que no tenga nada mas
    def __init__(self, nombre="", apellido="", edad="", idioma=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.idioma = idioma


    def saludar(self): #metodo, acciones oo funciones
        print(self.nombre, " esta saludando")
    def preguntar(self): #metodo, acciones oo funciones
        print(self.nombre, " -¿como estas?")
    def responder(self): #metodo, acciones oo funciones
        print(self.nombre, " - Muy bien")
    def comer(self):
        print(self.nombre, " esta comiendo")
    def dormir(self):
        print(self.nombre, " esta durmiendo")

jony = Persona("jontan", "Ariste", 38, "esp") #jony instancia la clase persona, y hereda todos sus metodos (funciones)

dario = Persona("dario", "ochoa", 31, "ESP") #los atributos de init

print(type(jony))

jony.saludar()

dario.comer()

#como modificar atributos
dario.edad = 18

print("dario tiene", dario.edad)


print("\n\n --------- conversación ----------")
jony.saludar()
dario.preguntar()
jony.responder()