"""abstraccion:
es el pilar de la poop, que permite identificar las caracteristicas t comportameintos de un objeto y con los 
cuales se construira la clase (plantilla), esto quiere decir que a travez de este pilar o fundamento
es posible reconocer los atributos y metodos de un objeto
"""

class Alumno:
    def __init__(self, nombre, apellido, anio_cursado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__anio_cursado = anio_cursado

    def cambiar_de_anio(self, anio):
        self.__anio_cursado = anio
    
    def mostrar(self):
        print(f'El alumno {self.__nombre} {self.__apellido} esta cursando {self.__anio_cursado} año en la institucion Incluit')

    """
    Encapsulamiento:
    es la caracteristica que permite el ocultamiento de  la complejidad del cofigo
    pertenece a la parte privada de la clase que no puede ser vista ni moficada por ningun otro programa
    """

    @property
    def apellido(self):
        return self.__apellido


    def set_apellido(self, apellido):
        self.__apellido = f"{apellido} (modificado)"


class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
#Un solo _ en el atributo va a habilitar a las clases dentro del mismo paquete a verlos/modificarlos

class Profesor(Persona):
    def __init__(self, nombre, apellido, legajo):
        super().__init__(nombre, apellido) #se pasan los parametros a la clase paadre para que  inicialice los atributos
        self.__legajo = legajo

    def mostrar(self):
        print(f'El profesor {self._nombre} {self._apellido} tiene el numero de legajo : {self.__legajo}')

"""Herencia:
es le pilar mas fuerte que asegura la reutilizacion de codigo..
a partir de esto es posible que las clases hijas hereden comportameinto y caracteristicas de clases padre.
clase hija -- clase derivada
clase padre """

"""
Polimorfismo:
Son comportamientos diferentes asociados a objetos distintos pero que pueden compartir el mismo nombre.
al llamrlos por ese nombre se utilizará el comportamiento correspondiente al objeto que se este usando
"""

class Animal:
    def __init__(self):
        patas = int(input("ingrese cantidad de patas"))
        self.cantidad_patas = patas

    def hablar(self):
        print("yo hablo")

class Perro(Animal):
    def __init__(self):
        super().__init__()

    def hablar(self):
        print("guau guau")

class Gato(Animal):
    def __init__(self):
        super().__init__()
    
    def hablar(self):
        print("miau")

class Humano(Animal):
    def __init__(self):
        super().__init__()


# perro = Perro()
# gato = Gato()
# humano = Humano()

# perro.hablar()
# gato.hablar()
# humano.hablar()