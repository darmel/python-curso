#programa para ejercitar diversos temas como funciones, control de cadenas, listas, etc

#devuelve la longitud del string
class longitudCadena:
    @staticmethod
    def longitud(cadena):
        return (len(cadena))

print(longitudCadena.longitud('esto'))

#toma un caracter y devuelve True si es una vocal
class VocalToF:
    @staticmethod
    def vocal(caracter):
        i=False
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o'or caracter == 'u' :
            i = True
        elif caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':
            i = True
        else:
            i = False
        return(i)

print(VocalToF.vocal('e'))

print(VocalToF.vocal('r'))

#sumar y multiplicar todos los numeros de una lista
class Sumando:
    @staticmethod
    def sum(entrada):
        resultado=0
        for i in entrada:
            resultado=int(i)+resultado
        return(resultado)


lista = input('ingrese una lista de numeros para sumarlos')
#lista='1234'
list1=[]
list1[:0]=lista
print(list1)

print(Sumando.sum(list1))

lista = input('ingrese una lista de numeros para multiplicarlos ')
#lista='1234'
list1=[]
list1[:0]=lista
print(list1)

class Multiplicando:
    @staticmethod
    def multiplica(entrada):
        resultado=1
        for i in entrada:
            resultado=int(i)*resultado
        return(resultado)

print(Multiplicando.multiplica(list1))