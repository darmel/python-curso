'''5) Dados 3 números, determinar si la suma del primero y 
el segundo es igual al tercero. Si se cumple, escribir 
"La suma es igual al tercero", si no, escribir 
"La suma es distinta al tercero".'''

numero_1 = int(input('ingrese el primer número: '))
numero_2 = int(input('ingrese el segundo número: '))
numero_3 = int(input('ingrese el tercer número: '))

if numero_1+numero_2 == numero_3 :
    print('La suma es IGUAL al tercer numero')
else:
    print('La suma es DISTINTA del tercer numero')
