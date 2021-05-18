'''parametros o argumentos
son valores que se reciben en una funcion a travez de los parentesis)'''

def nombre_funcion(param):
    valor = 0
    return valor


def mostrar_usuario(nombre, edad, ciudad):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

mostrar_usuario('santiago',37,'villa carlos paz')

mostrar_usuario(nombre='santiago',ciudad='villa carlos paz',edad=37)

#funcion con parametros opcionales
#en la definicion de la funcion se le da un valor por defecto a la variable de parametro
def mostrar_usuario_opcional(nombre, edad, ciudad='Cordoba'):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

mostrar_usuario_opcional('santiago',37)


'''Funciones con retorno
son funciones que retornan un valor para ser usado en otra funcion'''
def funcion_cuadrado_mayor()
