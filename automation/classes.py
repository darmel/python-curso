class Personaje:

    # constructor:        (atributos necesarios para iniicalizar)
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def get_fuerza(self):
        return self.__fuerza

    def get_defensa(self):
        return self.__defensa

    def get_inteligencia(self):
        return self.__inteligencia

    def atributos(self):
        print(self.__nombre, ":", sep='')
        print("-Fuerza: ", self.__fuerza)
        print("-Inteligencia: ", self.__inteligencia)
        print("-Defensa: ", self.__defensa)
        print("-Vida: ", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza+fuerza
        self.__inteligencia = self.__inteligencia+inteligencia
        self.__defensa = self.__defensa+defensa

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def dano(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.__vida = enemigo.__vida - dano
        print(self.__nombre, "ha realizado", dano,
              "puntos de daño a ", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__espada = espada

    def cambiar_arma(self):
        opcion = int(
            input("elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.__espada = 8
        elif opcion == 2:
            self.__espada = 10
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Espada: ", self.__espada)

    def dano(self, enemigo):
        return self.get_fuerza() * self.__espada - enemigo.get_defensa()

    def test(self):
        # print(self.__fuerza)
        print(self.get_fuerza())
        print(self.__espada)
        print(self.get_fuerza()*self.__espada)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__libro = libro

    def atributos(self):
        super().atributos()
        print("-Libro: ", self.__libro)

    def dano(self, enemigo):
        return self.get_inteligencia()*self.__libro-enemigo.get_defensa()


mi_personaje = Personaje("Darmel", 12, 1, 5, 100)
mi_enemigo = Personaje("Ennemy", 8, 5, 3, 3)
mi_personaje.nombre = "Darmel"
# mi_personaje.fuerza = 10
# print(mi_personaje)
# print("el nombre del personaje es ", mi_personaje.nombre)
# print("la fuerza del personaje es ", mi_personaje.fuerza)

# mi_personaje.atributos()  # llamo al metodo "atributos()"
# llamo al metodo subir nivel y le paso los valores necesarios
mi_personaje.subir_nivel(1, 2, 0)
# mi_personaje.atributos()  # vuelvo a mostrar todos los atributos
# mi_enemigo.atributos()  # muestro atributos de enemigo
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.atributos()

goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
vanessa = Mago("Vanessa", 20, 15, 10, 100, 5)
goku.atributos()
guts.atributos()
vanessa.atributos()

# guts.test()
goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)
guts.atacar(goku)


goku.atributos()
guts.atributos()
vanessa.atributos()
#
