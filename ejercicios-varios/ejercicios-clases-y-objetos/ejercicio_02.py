import random

class Vivienda:
    def __init__(self):
        self._n_vivienda = input("ingrese el numero de vivienda: ")
        self._direccion = input("ingrese la direccion: ")
        self._precio = 0

    def asignar_precio(self):
        self._precio = int(round(random.uniform(120000,150000),0))

    def mostrar_vivienda(self):
        print(f"""------------------
        el numero de vivienda es: {self._n_vivienda}
        la direccion es: {self._direccion}
        el precio es: {self._precio}
        """)

class Casa(Vivienda):
    def __init__(self):
        super().__init__()
        self._n_ambientes = input("ingrese el numero de ambientes: ")
        self._n_dormitorios = input("ingrese el numero de dormitorios: ")
        self._pileta = False  if input("ingrese 0 si la casa NO posee pileta, en caso afirmativo ingrese 1: ") == '0' else True #cambiar True y Flase por 'Si' y 'No'?
        self._superficie = input("ingrese la superficie en m2: ")
        self._amueblada = False  if input("ingrese 0 si la casa NO esta amueblada, en caso afirmativo ingrese 1: ") == '0' else True #cambiar True y Flase por 'Si' y 'No'?

    def precio_financiado(self):
        self._precioFinanciado = self._precio * 1.5

    def mostrar_casa(self):
        print(f"""------------------
        el numero de vivienda es: {self._n_vivienda}
        la direccion es: {self._direccion}
        el precio es: {self._precio}
        numero de ambientes es: {self._n_ambientes}
        numero de dormitorios es: {self._n_dormitorios}
        posee pileta: {self._pileta}
        la superficie total es de: {self._superficie} m2
        se encuentra amueblada: {self._amueblada}
        precio financiado: {self._precioFinanciado})
        """)

class Departamento(Vivienda):
    def __init__(self):
        super().__init__()
        self._n_ambientes = input("ingrese el numero de ambientes: ")
        self._n_dormitorios = input("ingrese el numero de dormitorios: ")
        self._asador = False  if input("ingrese 0 si el departamento NO posee asador, en caso afirmativo ingrese 1: ") == '0' else True #cambiar True y Flase por 'Si' y 'No'?
        self._superficie = input("ingrese la superficie en m2: ")
        self._amueblada = False  if input("ingrese 0 si el departamento NO esta amueblado, en caso afirmativo ingrese 1: ") == '0' else True #cambiar True y Flase por 'Si' y 'No'?

    def precio_financiado(self):
        self._precioFinanciado = self._precio * 1.2
    
    def mostrar_departamento(self):
        print(f"""------------------
        el numero de vivienda es: {self._n_vivienda}
        la direccion es: {self._direccion}
        el precio es: {self._precio}
        numero de ambientes es: {self._n_ambientes}
        numero de dormitorios es: {self._n_dormitorios}
        posee asador: {self._asador}
        la superficie total es de: {self._superficie} m2
        se encuentra amueblado: {self._amueblada}
        precio financiado: {self._precioFinanciado}
        """)

