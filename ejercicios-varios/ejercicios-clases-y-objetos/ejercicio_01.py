class Alquiler:
    def __init__(self):
        self.__marca = input("ingrese la marca: ")
        self.__modelo = input("ingrese la modelo: ")
        self.__anio = input("ingrese el anio: ")
        self.__precioKm = int(input("ingrese el precio por Km: "))
        self.__precioSeguro = int(input("ingrese precio del Seguro: "))
        self.__dni = input("ingrese la DNI del arrendatario: ")
        self.__nombreArrendatario = input("ingrese nombre del arrendatario: ")
        self.__kmRecorridos = int(input("ingrese Kilometros recorridos: "))


    def mostrar_alquiler(self):
        print(f"""------------------
        la marca es: {self.__marca}
        el modelo es: {self.__modelo}
        del año: {self.__anio}
        el precio por Km reccorido eses: {self.__precioKm}
        el precio del seguro es: {self.__precioSeguro}
        el DNI del Arrendatario es: {self.__dni}
        el nombre del arrendatario es: {self.__nombreArrendatario}
        los Km recorridos fueron: {self.__kmRecorridos}
        el valor total del alquiler es: {self.__kmRecorridos*self.__precioKm+self.__precioSeguro}
        """)