#clasica calculadora para utilizar while, funciones, if
#las funciones hay que definirlas antes de utilizarlas 

#funciones
def ingresar():
    num=int(input("ingrese un numero: "))
    return(num)

def sumar(num1, num2):
    return (num1 + num2)

def restar(num1, num2):
    return (num1 - num2)

def multiplicar(num1, num2):
    return (num1 * num2)

def dividir(num1, num2):
    return (num1 / num2)



#main
nombre = input("Ingresa tu nombre: ")
#inicio = 'empezar'
inicio = input("bienvenido "+ nombre + " escribe \"empezar\" para arrancar el programa: ")
print(inicio)
while (inicio == 'empezar'):
    print('Esto es una calculadora, elige la opcion que quieras')
    print("""
    1 - Sumar, la operación basica
    2 - Restar, 
    3 - Multiplicar, como sumar pero más rapido
    4 - Dividir, cuidado con los numeros que ingresas
    5 - Salir""")

    opcion = input()

    if opcion == '1' :
        num1, num2  = ingresar(), ingresar()
        print("el resultado de la suma es: ", sumar(num1, num2)) 

    elif  opcion == '2' :
        num1, num2  = ingresar(), ingresar()
        print("el resultado de la resta es: ", restar(num1, num2)) 

    elif opcion == '3' :
        num1, num2  = ingresar(), ingresar()
        print("el resultado de la multiplicacion es: ", multiplicar(num1, num2)) 

    elif opcion == '4' :
        num1, num2  = ingresar(), ingresar()
        if num2 == 0:
            print('la operacion no se puede realizar')
        else:
            print("el resultado de la suma es: ", dividir(num1, num2)) 
    
    elif opcion == '5':
        print('Gracias por utilizar la chotiCalculadora')
        inicio = ''
    
    else :
        print('Debe elegir una opcion entre 1 y 5')





