import json
from pprint import pprint
import json
from pathlib import Path
import requests


def obtain_person_by_lastname(unique_last_name, people):
    return [person for person in people if person['lname']
            == unique_last_name]  # new_user va a ser igual a person si lname == unique_last_name, y esto lo prueba para cada person en people


# funcion para mejkor visualizacion de estructuras de datos, diccionarios
# listas, JSONs, etc
# imprime una linea en blanco (por el print())
# luego el msg formateado con ident = indetn
# modifique el print para que use json.dumps porque me gusta más


def pretty_print(msg, indent=4):
    print()
    pprint(msg, indent=indent)


BASE_PATH = Path.cwd().joinpath('tests', 'data')
# print("Directoroio actual: ", BASE_PATH)


def read_file(file_name):
    path = get_file_with_json_extension(file_name)

    with path.open(mode='r') as f:
        # lee el archivo (f) y devuelve un python object (dictionary)
        return json.load(f)


# verifica la extension del archivo

def get_file_with_json_extension(file_name):
    if '.json' in file_name:
        path = BASE_PATH.joinpath(file_name)
    else:
        path = BASE_PATH.joinpath(f'{file_name}.json')
    return path

# limpia la base de datos


def db_cleaner():
    id = 4
    while id < 100:
        url = 'http://127.0.0.1:5000/api/people/'
        respose = requests.delete(f'{url}/{id}')
        id = id + 1
