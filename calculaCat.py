#calculadora de edad de gatos
#Programa para calcular aproximadamente la edad de tu gato en 
#años gatunos

nombre = str(input('Ingrese el nombre de su mascota felina: '))
genero = str(input('ingrese el genero de su mascota felina: '))
edad = float(input('ingrese la edad de su mascota felina en años: '))

def calcularEdad(nombre, genero, edad):
    if genero == 'macho':
        sufijo = 'o '
    elif genero == 'hembra':
        sufijo = 'a '
    else:
        sufijo = 'x '

    if edad <= 1 :
        print('su gat',sufijo, nombre,' es muy MUY joven.', sep='')

    elif edad < 2 :
        print('su gat',sufijo, nombre,' es joven. Aun no es adulto, tiene alrededor de 20 años', sep='')

    elif edad <= 2 :
            print('su gat',sufijo, nombre,' tiene 24 años.', sep='')

    elif edad < 4 :
        print('su gat',sufijo, nombre,' tiene alrededor de 28 años', sep='')

    elif edad <= 4 :
            print('su gat',sufijo, nombre,' tiene 32 años.', sep='')

    if edad > 4 :
        edad = int(24 + (edad-2)*4)
        print('su gat',sufijo, nombre, ' tiene ',edad,' años.', sep='')



calcularEdad(nombre, genero, edad)

print('\n ---------------\n -----datos de prueba-------- \n -------------------\n ')
calcularEdad('1h', 'hembra', float(1))
calcularEdad('2m', 'macho', float(2))
calcularEdad('3o', 'otro', float(3))
calcularEdad('4h', 'hembra', float(4))
calcularEdad('5h', 'hembra', float(5))
calcularEdad('6h', 'hembra', float(6))
calcularEdad('7m', 'macho', float(7))
calcularEdad('8o', 'otro', float(8))
calcularEdad('9h', 'hembra', float(9))
calcularEdad('10m', 'macho', float(10))
calcularEdad('12o', 'otro', float(12))
calcularEdad('14h', 'hembra', float(14))
calcularEdad('16m', 'macho', float(16))
calcularEdad('18o', 'otro', float(18))
calcularEdad('20h', 'hembra', float(20))
calcularEdad('22h', 'hembra', float(22))