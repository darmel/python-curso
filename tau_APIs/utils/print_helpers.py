import json
from pprint import pprint

# funcion para mejkor visualizacion de estructuras de datos, diccionarios
# listas, JSONs, etc
# imprime una linea en blanco (por el print())
# luego el msg formateado con ident = indetn
# modifique el print para que use json.dumps porque me gusta más


def pretty_print(msg, indent=4):
    print()
    pprint(msg, indent=indent)
    # print(json.dumps(msg, indent=indent))
