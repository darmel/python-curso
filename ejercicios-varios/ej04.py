'''4) Determinar si un número ingresado es: negativo, cero
o positivo e imprimir, de acuerdo a cada caso,
el mensaje correspondiente.'''

numero = int(input('ingrese un número: '))
if numero < 0 :
    print(f'el numero {numero} es negativo')
elif numero == 0 :
    print('el numero es 0')
else:
    print(f'el numero {numero} es positivo')
