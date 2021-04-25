#clases
#class (palabra reservada) El nombre de la clase comienza en mayuscula
class Persona: 
    #pass //pass es para que no tenga nada mas
    def saludar(self, nombre): #metodo, acciones oo funciones
        print(nombre, " esta saludando")
    def comer(self, nombre):
        print(nombre, " esta comiendo")
    def dormir(self, nombre):
        print(nombre, " esta durmiendo")

jony = Persona() #jony instancia la clase persona, y hereda todos sus metodos (funciones)

dario = Persona()

print(type(jony))

jony.saludar("Jony")

jony.dormir("jony")

dario.comer("dario")