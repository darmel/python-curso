def ejercicio_1_for_en_vector():
    nombres = ['Lucas','Franco','Luciano','Malena','Jonatan','Luciano','Rodrigo','Maria']
    for i in nombres:
        print(i)


def ejercicio_2_for_con_incremento():
    for j in range(1,11):
        print(j,end=', ') 
    print('\b\b ')

def ejercicio_3_for_con_decremento():
    for l in range(9,-1,-1):
        print(l,end=', ') 
    print('\b\b ')


def ejercicio_4_while():
    m=0
    nota=0
    notas=0 
    nota=int(input('Ingrese el valor de la nota o 0 para terminar: '))

    while nota != 0 :
        m=m+1
        notas=notas+nota
        nota=int(input('Ingrese el valor de la nota o 0 para terminar: '))

    '''print('notas:', notas)
    print('nota:', nota)
    print('m:', m)'''
    if m != 0 :
        print('el promedio de las notas ingresadas es: ', notas/m)
    else:
        print('no existen notas cargadas')


print('-----Ejercicios con Loops------\n\n')
print('''Ejercicio 1:
Nombre de la función: ejercicio_1_for_en_vector
En esta función agregar el vector: nombres = [‘Lucas’,’Franco’,’Luciano’,’Malena’,’Jonatan’,’Luciano’,’Rodrigo’,’Maria’]
Recorra el vector e imprima los elementos utilizando el ciclo for\n''')
ejercicio_1_for_en_vector()

print('''\n\nEjercicio 2:
Nombre de la función: ejercicio_2_for_con_incremento
La función debe imprimir la siguiente serie de números: 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 \n''')
ejercicio_2_for_con_incremento()

print('''\n\nEjercicio 3:
Nombre de la función: ejercicio_3_for_con_decremento
La función debe imprimir la serie de números: 
9, 8, 7, 6, 5, 4, 3, 2, 1, 0 \n''')
ejercicio_3_for_con_decremento()


print('''\n\nEjercicio 4:
Nombre de la función: ejercicio_4_while
Realice una función que mientras la nota ingresada sea distinta de 0 le solicite al profesor el ingreso de otra nota,
una vez que el profesor ingrese la nota 0 deberá imprimir un mensaje con el promedio de todas las notas ingresadas\n''')
ejercicio_4_while()