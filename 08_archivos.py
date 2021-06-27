from pilares_poo_08_for_archivos import Persona
import json

def escribir_en_archivo():
    persona = Persona('Santiago', 'Pasalaqua')
    file_name = "./data/santiago.json"
    #archivo = open("./data/santiago.json") #por defecto abre en modo lectura, si no existe devuelve error. mode='r'
    # mode='a' (append) se abre y solo se le puede agregar data
    archivo = open(file=file_name, mode='w') #modo escritura, si no existe lo crea
    archivo.write(persona.to_json())
    archivo.close()

    persona_guardada = open(file_name, 'r') #lee y guarda el archivo en "persona_guardad"
    persona_json = json.load(persona_guardada) #load guarda como objeto, .loads guarda como string

    print(persona_json)
    persona_json['_direccion'] = 'Alejandria'
    print(persona_json)
    persona_json['_nombre'] = 'Juan'
    print(persona_json)
    
escribir_en_archivo()