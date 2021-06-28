from clases import Transaccion

lista_transacciones = []

def opciones_menu():
    opcion = int(input("""\nIngrese la opcion elegida: 
    1. Listar transacciones
    2. Verificar justificación de movimientos
    3. Imprimir transacciones con monto mayor a 100000
    4. Sumar los montos de todas las transacciones cuyo tipo_movimiento sea igual a CONSUMO
    0 Salir
    : """))
    return opcion

def menu():
    transaccion_a = Transaccion(45990339, 'CONSUMO', 2000, 'RECHAZADO', 'MUSIMUNDO')
    transaccion_b = Transaccion(45990339, 'CONSUMO', 2000, 'APROBADO', 'MUSIMUNDO')
    transaccion_c = Transaccion(30949303, 'CASH_IN', 50000, 'APROBADO', 'PAGOFACIL')
    transaccion_d = Transaccion(30949303, 'CASH_OUT', 300000, 'APROBADO', 'PAGOFACIL')
    lista_transacciones.append(transaccion_a)
    lista_transacciones.append(transaccion_b)
    lista_transacciones.append(transaccion_c)
    lista_transacciones.append(transaccion_d)


    op=1
    while op != 0 :
        op = opciones_menu()
        if op == 1:
            i=0
            for item in lista_transacciones:
                print('--------------')
                lista_transacciones[i].mostrar_transaccion()
                i=i+1
        
        elif op == 2:
            i=0
            for item in lista_transacciones:
                print('--------------')
                print(lista_transacciones[i].verificacion())
                i=i+1
        
        elif op == 3:
            i=0
            print('Transacciones superiores a 100000')
            for item in lista_transacciones:
                if lista_transacciones[i].get_monto() > 100000:
                    print(f'La transaccion {lista_transacciones[i].get_id()} posee monto de {lista_transacciones[i].get_monto()}')
                i=i+1

        elif op == 4:
            i=0
            suma=0
            print('Suma de transacciones del tipo CONSUMO')
            for item in lista_transacciones:
                if lista_transacciones[i].get_tipo() == 'CONSUMO':
                    suma=suma+(lista_transacciones[i].get_monto())
                i=i+1
            print('la suma de todos los montos de trasacciones de tipo CONSUMO es:', suma)
        
        elif op == 0:
            print("Gracias por utilizar este software")
        
        else :
            print('Opcion invalida, intente nuevamente')

        

menu()
