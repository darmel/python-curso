'''listas
coleccion de datos 
pueden contener distintos tipos de datos
pueden tener otras colecciones(listas, diccionarios, tuplas) como elementos
dentro de la lista
Es mutable: se pueden agregarm remover o cambiar elementos
Pueden mantener un orde, por lo que se puede acceder  a los elementos 
mediante un indice'''

frutas = ['manzana', 'peras', 'durazno']
años  = [3,'1998',2.5,234,943] 
numeros = [3,1998,2.5,234,943]


def mostrar_con_for(lista):
    for fruta in lista:
        print(lista)

    cant_elementos = len(lista)
    for i in range (0,cant_elementos):
        print(f"Elemento en posicion{i} = {lista[i]}")

frutas.append("naranja")
print(frutas)

'''remueve un elemento de la lista'''
print(frutas)
frutas.remove(manzana)
print(frutas)

'''elimina el elelemnto en el indice indicado'''
print(frutas)
rutas.pop(1)
print(frutas)

'''agrego elementos'''
print(frutas)
furtas.insert