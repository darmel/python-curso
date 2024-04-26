'''programacion arientada a objetos.
todo puede ser un objeto.
un objeto es un concepto o una cosa con un significado o limites claros en el 
problema en cuestion
Un objeto tiene:
    un stado: lo que el objeto sabe, lo que es. Esta dado por las variables. Cambia a lo largo del tiempo
            
    un compartamiento: como actua el objeto, 

Que es una clase?
    "un molde para hacer objetos"
    es una descripcon de un grupo de objetos con:
        propiedades en comun
        comportameinto similar
        la misma forma de relacionarse con otros objetos
        una semantica en  comun
    Una clase es una abstraccion que
        enfatiza las caracteristicas relevantes
        suprime otras caracteristicas.

Un OBJETO es una instancia de una clase.

Una clase es una definicion abstracta de un objeto
    define la estructura
    comportamientos
'''
#por convencion las clases de escriben en CamelCase

'''def __init__(self) se usa para crear instancias de una clase con parametros especificos
    Asignamos los valores a los atributos
    es requerido(peude estar o no) pero se usa para asignar el estado por defecto de los objetos
    es el primer metodo de la clase

    self:representa a la instancia de la clase, lo usamos para hcer referecnai a las variables y estados de la clase
    de esta manera podemos compartir informacion eficiente y facilmente dentro de una clase
'''
class Persona: 
    def __init__(self, nombre, apellido, empresa='Incluit'):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__empresa = empresa

    def presentarse(self):
        print(f"Hola, mi nombre es {self.__nombre} {self.__apellido} y trabajo en {self.__empresa}")

    def incorporarse_a_incluit(self):
        self.__empresa = 'Incluit'

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_nombre(self):
        return self.__nombre

#class Alumno(Persona): #alumno hereda atributos y metodos def persona