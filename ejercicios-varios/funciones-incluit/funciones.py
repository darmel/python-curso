def menor_diez():
    numero = int(input('ingrese un número: '))
    if numero > 10:
        print(f'el numero {numero} es mayor que 10')
    else:
        print(f'el numero {numero} es menor o igual a 10')

def suma_dos(num1, num2, num3):
    if num1+num2 == num3 :
        print('La suma es IGUAL al tercer numero')
    else:
        print('La suma es DISTINTA del tercer numero')


def cuadrado_mayor(numero_1, numero_2):
    if numero_1 > numero_2 :
        return ((numero_1*numero_1) / (numero_2*numero_2))
    elif numero_2 > numero_1 :
        return ((numero_2*numero_2) / (numero_1*numero_1))
    else:
        return 1


def far_to_cel():
    temp_f = int(input('ingrese una temperatura en °F: '))
    temp_c = round((5/9)*(temp_f-32))

    return temp_c

'''menor_diez()
suma_dos(5,5,10)
suma_dos(5,5,11)
print(cuadrado_mayor(4,2))
print(cuadrado_mayor(4,4))
print(far_to_cel())'''