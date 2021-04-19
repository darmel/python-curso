#tuplas, son inmutables. 
#son mas rapidas que las listas
#pueden contener cualqueir tipo de datos, incluso listas y otras tuplas

lista = ['a','b','c']

miTupla = (1,2,3,4,5,lista)

tuplaDos = ('perro','gato','canario',miTupla)

print(tuplaDos)

lista.append('casa')

print(tuplaDos)
