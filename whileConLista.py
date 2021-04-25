#bucle de control WHILE con listas

numero = int(input('ingrese el primer numero: '))

total=0
listaDeNumeros = []

while numero != 0 :
    listaDeNumeros.append(numero)
    total += numero
    numero = int(input('ingrese otro numero para sumar o 0 para terminar:  '))
    
print('la suma total es de: ', total)
print('se sumaron los siguientes numeros: ',listaDeNumeros)