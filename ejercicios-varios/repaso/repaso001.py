# print("-Primer ejercicio")
# print("ingrese su nombre:")
# nombre = input()
# print("ingrese su edad:")
# edad = input()
# if int(edad) >= 18:
#     print("hola", nombre, "de", edad, "años de edad. Eres MAYOR de edad. el ejercicio 1 esta resuielto")
# else:
#     print("hola", nombre, "de", edad, "años de edad. Eres MENOR de edad. el ejercicio 1 esta resuielto")
# 
# print("Segundo ejercicio")
# vocales = 0
# vocales_para_comparar = "aeiouAEIOU"
# print("ingrese una oración")
# cadena = input()
# print("la cadena ingresada es:", cadena)
# 
# for i in cadena:
#     if i in vocales_para_comparar:
#         vocales += 1
# 
# print("La cadena contiene", vocales, "vocales")
# 
# 

#print("3er ejercicio")
#
#personas = [
#    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#    {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona"},
#    {"nombre": "Luis", "edad": 22, "ciudad": "Madrid"},
#    {"nombre": "María", "edad": 28, "ciudad": "Valencia"},
#    {"nombre": "Carlos", "edad": 35, "ciudad": "Sevilla"},
#    {"nombre": "Laura", "edad": 29, "ciudad": "Bilbao"},
#    {"nombre": "Pedro", "edad": 40, "ciudad": "Bilbao"},
#    {"nombre": "Sofía", "edad": 27, "ciudad": "Zaragoza"},
#    {"nombre": "Diego", "edad": 33, "ciudad": "Murcia"},
#    {"nombre": "Elena", "edad": 26, "ciudad": "Palma de Mallorca"},
#    {"nombre": "Javier", "edad": 31, "ciudad": "Las Palmas"},
#    {"nombre": "Marta", "edad": 24, "ciudad": "Valladolid"},
#    {"nombre": "Pablo", "edad": 32, "ciudad": "Valencia"},
#    {"nombre": "Lucía", "edad": 23, "ciudad": "Alicante"},
#    {"nombre": "Raúl", "edad": 34, "ciudad": "Vigo"}
#]
#i = 0
#print("esta es la lista de ciudades: ")
#for dict in personas:
#    print(dict["ciudad"])
#
#print("Ingrese un nombre de Ciudad")
#ciud = input()
#
#print("las personas que vivien en esa ciudad son:")
#
#for dict in personas:
#    if dict["ciudad"] == ciud:
#        print(dict["nombre"])
#

#Repaso de manipular archivos

#abir archivo de text
def mostrar_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        print(archivo.read())

with open("archivo.txt", "a") as archivo:
    archivo.write("esta es una nueva linea")

#mostrar_archivo()

#abrir. leer y escribir archivo JSON

import json
from pprint import pprint

def mostrar_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        datos = json.load(archivo)
        print(json.dumps(datos, indent=4))

persona = {"nombre": "Pedro", "edad": 12, "ciudad": "Vallecas"}

#modificar json
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

#print(datos)

datos[0]["edad"] += 1

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4) #reescribe el objeto python datos en el archivo usando formato json


# agregar data al archivo json, hay que cargarlo en un objeto python, agregarle la data nueva como objeto python,
# reescribir el json volcando el nuevo objeto python a un archivo json.

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
   # print(datos)
   # print(persona)
    datos.append(persona)
   # print(datos)

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)


#mostrar_json("datos.json")


#ejercicio 5
nuevo_estudiante = {"nombre": "Marta", "edad": 12, "curso": "Literatura"}


with open("estudiantes.json", "r") as archivo:
    datos = json.load(archivo) #cargo el objeto json en datos (como un objeto python)
    #print(datos) 
    datos.append(nuevo_estudiante) #agrego el objeto pytohn nuevo estudiante, al otro objeto python datos
   # print(datos)

with open("estudiantes.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

#mostrar_json("estudiantes.json")

#ejercicio 6

credenciales = []
print(credenciales)

with open("registros.txt", "r") as archivo:
    #print(archivo.read()) #lo saco para qeu el cursor del python leyendo el archivo no quede al final
    for linea in archivo:
        usuario, contrasena = linea.strip().split(":")
        credenciales.append({"usuario": usuario, "contraseña:": contrasena})

with open("credenciales.json", "w") as archivo:
    json.dump(credenciales, archivo, indent=4)

mostrar_json("credenciales.json")
        
#print (credenciales)