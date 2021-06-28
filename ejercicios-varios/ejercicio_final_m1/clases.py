import random

class Transaccion:
    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self._transaccion_id = random.randrange(1,  99999999)
        self._dni_cliente = dni_cliente
        self._tipo_movimiento = tipo_movimiento
        self._monto_movimiento = monto_movimiento
        self._estado = estado
        self._nombre_comercio = nombre_comercio

    def mostrar_transaccion(self):
        print(f"""
        ID: {self._transaccion_id}
        dni cliente: {self._dni_cliente}
        estado: {self._estado}
        monto: {self._monto_movimiento}
        nombre de comercio: {self._nombre_comercio}
        tipo de movimiento: {self._tipo_movimiento}""")

    def verificacion(self):
        id=str(self._transaccion_id)
        if self._monto_movimiento < 100000 :
            return(f'El movimiento {id} no requiere justificacion')
        else :
            return(f'Se debe solicitar documentacion que requiera la justificacion del  movimiento: {id} ')

    def get_monto(self):
        return(self._monto_movimiento)

    def get_id(self):
        return(self._transaccion_id)

    def get_tipo(self):
        return(self._tipo_movimiento)