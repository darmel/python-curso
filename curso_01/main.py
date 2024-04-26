#import clases_4
from clases_4 import Triangulo
import clases_5

def app():
    print("Hola mundo")
    #print(clases_4.Triangulo.area(10,20))
    print(Triangulo.area(10,20)) #si uso "from" llamo el metodo así
#traer de clases_4.py traje la clase Triangulo y llamo el metodo area.
    print (clases_5.Circulo.area(15)) #acá importo todo el modulo, 
if __name__ == '__main__':
    app()