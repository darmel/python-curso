#Strings

cadena = 'Hola Mundo Loco DevRocker'

print(cadena)

#pasar to a mayusculas
print(cadena.upper())

#poner la primera letra en mayuscula
print(cadena.capitalize())

#Reemplazar pedazos por otros
print(cadena.replace('Loco','Pepe'))

#intercambia mayusculas por minusculas
print(cadena.swapcase())

#contar cuantas veces aparece un pedazo de string en un string
print(cadena.count('Loco'))
print(cadena.count('o'))

#preguntar si la cadena comienza con una palabra o letra
print(cadena.startswith('Hola'))

#preguntar si termina con una palabra o letra
print(cadena.endswith('ker'))

#cortar el string, y transformarlo en una lista con los elementos
print(cadena.split(' '))

#saber en que posicion esta letra o pedazo
print(cadena.find('Loco'))

#saber el tama;o en caracteres del strin
print(len(cadena))


