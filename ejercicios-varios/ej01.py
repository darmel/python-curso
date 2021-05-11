"""1) Escribir un algoritmo que lea un número entero y verifique
si es mayor a 10. Si lo es escribir el número y si no lo es 
escribir un mensaje que diga que el número es menor o igual"""

numero = int(input('ingrese un número: '))
if numero > 10:
    print(f'el numero {numero} es mayor que 10')
else:
    print(f'el numero {numero} es menor o igual a 10')