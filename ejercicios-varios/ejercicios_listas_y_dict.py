
frutas = ['manzana', 'peras', 'durazno']
verduras = ['acelga','lechuga']
alumnos = []
años= [1998, 1989, 1970, 2020, 1990]
jugador = {'comida': 15, 'energia': 100, 'enemigos':3}

'''solicitar que se ingresen los nombres de 10 alumnos, despues de ingresarlos se debe imprmir la lista'''
def ejercicio_1_cargar_lista(lista):
    for i in range(1,11):
        lista.append(input(f'Ingrese el nombre del alumno n°{i}: '))
    print(lista)

'''Esta función debe:
a. Pedir el ingreso de una nueva fruta e ingresarlo en la posición nro 2 de la lista de frutas, imprimir la nueva lista de frutas.
b. Unir a la lista de verduras todos los items en la lista de frutas, imprimir la lista de verduras
c. De la lista de verduras eliminar el item agregado en el inciso ‘a’ e imprimir la lista
d. De la lista de frutas eliminar la ultima fruta e imprimir la lista frutas'''
def ejercicio_2_modificar_lista(lfrutas, lverduras):
    nfruta = input('ingrese una nueva fruta: ')
    lfrutas.insert(2, nfruta)
    print('Lista de frutas: ', lfrutas)
    lverduras.extend(lfrutas)
    print('Lista de verduras y frutas: ', lverduras)
    lverduras.remove(nfruta)
    print('lista de verduras y frutas sin la nueva fruta: ', lverduras)
    lfrutas.pop() #elimino el ultimo elemento de lfrutas
    #print('Lista de frutas sin el último elemento', lfrutas.pop()) me muestra el elemenot que debería eliminar: consultar    print(lfrutas)
    print('Lista de frutas sin el último elemento', lfrutas)


'''Esta función debe:
e. Imprimir la lista
f. Ordenarla de forma ascendente e imprimirla de nuevo
g. Pedirle al usuario que ingrese un año y le responda si ese año se encuentra o no en la lista
h. En la lista ordenada, consultar en que index se encuentra el numero 1989'''
def ejercicio_3_ordenar_y_buscar_lista(numeros):
    print('lista original: ', numeros)
    numeros.sort()
    print('lista ordenada: ', numeros)
    nnumero=int(input('Ingrese un nuevo año: '))
    if nnumero in numeros:
        print(f'El año {nnumero} YA se encuentra en la lista')
    else:
        print(f'El año {nnumero} NO se encuentra en la lista')
    print('El año 1989 se encuentra en la posición: ', numeros.index(1989))

def ejercicio_4_diccionarios(player):
    print(player)
    print(player.keys())
    nuevas_armas = {'rocas': 4, 'flechas': 5}
    player.update(nuevas_armas)
    print(player)
    player['amigos'] = 10
    print(player)
    player['comida'] = 30
    print(player)
    print(player['energia'])

#ejercicio_1_cargar_lista(alumnos)

#ejercicio_2_modificar_lista(frutas, verduras)

#ejercicio_3_ordenar_y_buscar_lista(años)

ejercicio_4_diccionarios(jugador)