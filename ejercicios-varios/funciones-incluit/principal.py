from funciones import *

'''menor_diez()
suma_dos(5,5,10)
suma_dos(5,5,11)
print(cuadrado_mayor(4,2))
print(cuadrado_mayor(4,4))
print(far_to_cel())'''
opcion = 1

def menu():
    op=int(input('''
    Ingrese una opcion:
    1 - Menor de Diez
    2 - Es la suma de los 2 primeros igual al 3ero?
    3 - Division del cuadro del mayor en el cuadrado del menor
    4 - Conversor Fherenheit a Centigrados
    0 - para salir
    '''))
    print('opción ingresada: ', op)
    return op


while opcion != 0 :
    opcion=menu()
    if opcion==1:
        menor_diez()
    elif opcion==2:
        numero_1 = int(input('ingrese el primer número: '))
        numero_2 = int(input('ingrese el segundo número: '))
        numero_3 = int(input('ingrese el tercer número: '))
        suma_dos(numero_1,numero_2,numero_3)
    elif opcion==3:
        numero_1 = int(input('ingrese el primer número: '))
        numero_2 = int(input('ingrese el segundo número: '))
        print('''la division del cuadrado del mayor
en el cuadrado del menor es: ''', cuadrado_mayor(numero_1,numero_2) )
    elif opcion==4:
        print('La temperatura en grados Celcius es: ', far_to_cel())
    elif opcion==0:
        print('Muchas gracias por utilizarme')
    else:
        print('Opcion no disponible')
