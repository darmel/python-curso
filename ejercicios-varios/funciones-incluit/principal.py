from funciones import *

'''menor_diez()
suma_dos(5,5,10)
suma_dos(5,5,11)
print(cuadrado_mayor(4,2))
print(cuadrado_mayor(4,4))
print(far_to_cel())'''
opcion = 1

def menu():
    opcion=int(input('''
    Ingrese una opcion:
    1
    2
    3
    4
    0 - para salir
    '''))

#menu()

while opcion != 0 :
    menu()
    if opcion==1:
        menor_diez
    elif opcion==2:
        numero_1 = int(input('ingrese el primer número: '))
        numero_2 = int(input('ingrese el segundo número: '))
        numero_3 = int(input('ingrese el tercer número: '))
        suma_dos(numero_1,numero_2,numero_3)
    elif opcion==3:
        numero_1 = int(input('ingrese el primer número: '))
        numero_2 = int(input('ingrese el segundo número: '))
        cuadrado_mayor(numero_1,numero_2)
    elif opcion==4:
        print('La temperatura en grados Celcius es: ', far_to_cel())
    else:
        print('Opcion no disponible')
