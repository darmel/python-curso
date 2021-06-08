from ejercicio_01 import Alquiler

cont=0
op= 1
lista = []
#alquiler1 = Alquiler()
#alquiler1.mostrar_alquiler()

while op != 0 :
    op= int(input("""
    Elija una Opción para continuar:
    1. Cargar nuevo Alquiler
    2. Mostrar lista de Alquileres
    0. Finalizar
    """))
    if op == 1:
        #cont = cont +1
        alquiler = Alquiler()
        lista.append(alquiler)

    elif op ==2:
        i=0
        for alquiler in lista:
            print("Alquiler n°: ", i)
            lista[i].mostrar_alquiler()
            i = i+1
        
    elif op == 0:
        print("Gracios por utilzar este programa")

    else:
        print("Ingrese una opcion valida")
        