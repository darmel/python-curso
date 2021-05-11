"""2) Dados dos número enteros, se necesita saber el resultado 
de dividir el cuadrado del mayor de ellos y el cuadrado 
del menor de ellos. Si los números son iguales escribir un
mensaje."""

numero_1 = int(input('ingrese el primer número: '))
numero_2 = int(input('ingrese el segundo número: '))

if numero_1 > numero_2 :
    print('el resultado de dividir el cuadro del 1er numero en el cuadrado del 2do numero es: ', (numero_1*numero_1) / (numero_2*numero_2))
elif numero_2 > numero_1 :
    print('el resultado de dividir el cuadro del 2do numero en el cuadrado del 1er numero es: ', (numero_2*numero_2) / (numero_1*numero_1))
else:
    print('los numeros son iguales')