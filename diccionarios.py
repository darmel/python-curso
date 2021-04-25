#Diccionarios pueden almacenar tuplas, varialebls,  listas, diccionarios, strings, etc.
#son mutables
#no tienen indice, tienen llaves

# diccionario = {}
# diccionario2 = dict()

diccionario = {'edad':33, "nombre":"jonatan", "Apellido":"ochao"}


print("diccionario completo \n", diccionario)
print("-------------\n")
print("diccionario keys \n", diccionario.keys())
print("-------------\n")
print("diccionario valores \n", diccionario.values())

print("-------------\n\n\n\n")
#creamos diccionario vacio
dic = {}
#asignamos valores al diccionario
dic["nombre"] = "Dario"
dic["apellido"] = "ochoa"

#imprmio todo el diccionario
print(dic)
#imprimo solo los valores de la key apellido
print(dic["apellido"])
#cambio valor de key apellido
dic["apellido"]="Balcazar"
#imprimo nuevo valor
print(dic["apellido"])


#metodo get, si esta el key devuelve el valor, si no existe devuelve el 2do parametro
print("\n\n ---------Metodo get----------")
print(dic.get("apellido", "este valor no existe"))
print(dic.get("telefono", "este valor no existe"))

#metodo setdefault, si esta el key devuelve el valor, si no esta lo crea y le carga el valor 2do parametro
print("\n\n ---------Metodo set----------")
print(dic.setdefault("telefono", "4844235"))


#eliminar elementos del diccionario
print("\n\n ---------elimianr----------")
del dic["nombre"]
print(dic)
dic.pop("apellido")
print(dic)
#dic = {}
dic.clear()
print(dic)
