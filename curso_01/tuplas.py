#tuplas, son inmutables. 
#son mas rapidas que las listas
#pueden contener cualqueir tipo de datos, incluso listas y otras tuplas

# lista = ['a','b','c']

# miTupla = (1,2,3,4,5,lista)

# tuplaDos = ('perro','gato','canario',miTupla)

# print(tuplaDos)

# lista.append('casa')

# print(tuplaDos)

# colores = ('rojo', 'verde', 'amarillo','violeta', 'marron')

# uno, dos, tres,*cuatro = colores

# print(uno)
# print(dos)
# print(tres)
# print (cuatro)


lista = [11,12,13,14,15]
miTupla = (1,2,3,4,5,6,7,8,9,10)

combineta = zip(lista,miTupla)

nuevaTupla = tuple(combineta)

print(nuevaTupla)

listaNueva = list(miTupla)

print(listaNueva)