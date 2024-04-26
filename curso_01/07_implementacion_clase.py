from objetos import Persona

def crear_objeto():
    objeto = Persona("santiago", "Pasalaccua")
    objeto.presentarse()

    objeto_2 = Persona("juan", "perez", 'Vates')
    objeto_2.presentarse()
    objeto_2.incorporarse_a_incluit()
    objeto_2.presentarse()

    objeto_2.set_empresa("making sense")
    objeto_2.presentarse()

    print(f"La persona que se fue es {objeto_2.get_nombre()}")

crear_objeto()
