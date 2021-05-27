'''diccionarios
contenido: son pares de key/value
mutables
order: puede mantener un orden de entrada
sintaxis: llaves que contienen la key, : un valor, esos pares key/value son separados por ,
'''

años = {'Laila':1974, 'Matias':1997}

cosas = {'comida':15, 'energia':198, 'enemigos': 3}

#obtener el valor segun la key
print (años['Laila'])
print(años.get('Laila'))

#parametro opcional despues de la coma poner el vcalor que queres que retorne si no encuentra el elemento
print(años.get('Lail', 'inexistente'))

#imprime todos los elementos del dioccioanrip
print(años.items())
print(cosas.items())

#imprmie las keys del diccionario
print(años.keys())
print(cosas.keys())

#remueve el ultimo elemento del diccionario
print(años.items())
años.popitem()
print(años.items())

#remueve un elemento a partir de la key
print(años.items())
del años['Laila']
print(años.items())

#el metodo update actualiza los valores segun la key, si la key no existe no agrega el elemento
print(años.items())
años.update({'Santiago':1984}) #agrega el valor 1984 para la key Santiaho
años.update({'Laila':1984}) #actualiza el año de la key lista
print(años.items())

new_items = {'rocas':4, 'flechas':5}
cosas.update(new_items)
print(cosas.items())

#agrega un nuevo elemento al diccionario
#revisar... no funciona
print(años.items())
cosas.setdefault('Ariel', 1988)
print(años.items())

#actualizar el valor de una key en el diccionario, no no existe la agrega
años['Santiago'] = 1980
print(años.items())

