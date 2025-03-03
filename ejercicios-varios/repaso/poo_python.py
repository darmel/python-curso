print("ejercicio de POO")

#creo una clase llamada Personaje
class Personaje:
    nombre = "Default"
    fuerza = 0 
    inteligencia = 0
    defensa = 0
    vida = 0

    #crear metodo constructor de la clase Personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    #metodo para mostrar atributos
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa", self.defensa)
        print("- Vida", self.vida)

    def subir_nivel(self, inc_fuerza, inc_inteligencia, inc_defensa):
        self.fuerza = self.fuerza + inc_fuerza
        self.inteligencia = self.inteligencia + inc_inteligencia
        self.defensa = self.defensa + inc_defensa

    def esta_vivo(self):
        return self.vida > 0  
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def dano(self, enemigo):
        #print(self.fuerza - enemigo.defensa)
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida = enemigo.vida - dano
        print(self.nombre, "ha realizado", dano, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

#creao una clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    #neuvo constrctor para Guerrero para agregarle un atributo "espada"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self): #sobreescribimos el metodo atributos
        super().atributos() #llamamos al metodo atributos del padre
        print("- Espada:", self.espada) #agregamos para espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10. (3) Daga, daño 5\n"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número incorrecto")

    def dano(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def dano(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
        


goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
rosa = Mago("Rosa", 20, 15, 10, 100, 5)

def combate(jugador_1, jugador_2):
    turno=1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno:", turno)
        print("Accion de ", jugador_1.nombre, ":")
        jugador_1.atacar(jugador_2)
        print("Accion de ", jugador_2.nombre, ":")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
        input("\nIngrese cualquier tecla para continuar")
    if jugador_1.esta_vivo():
        print("\nEl ganador es: ", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nEl ganador es: ", jugador_2.nombre)
    else:
        print("\nEmpate")


combate(guts, rosa)