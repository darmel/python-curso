from ejercicio_02 import *

cont=0
op= 1
listaCasas = []
listaDepto = []
#alquiler1 = Alquiler()
#alquiler1.mostrar_alquiler()

while op != 0 :
    op= int(input("""
    Elija una Opción para continuar:
    1. Cargar nueva Casa
    2. Cargar nuevo Departamento
    3. Mostrar lista de Casas
    4. Mostrar lista de Departamentos
    0. Finalizar
    """))
    if op == 1:
        vivienda = Casa()
        vivienda.asignar_precio()
        vivienda.precio_financiado()
        listaCasas.append(vivienda)

    elif op == 2:
        vivienda = Departamento()
        vivienda.asignar_precio()
        vivienda.precio_financiado()
        listaDepto.append(vivienda)

    elif op ==3:
        i=0
        for vivienda in listaCasas:
            print("Casas : ")
            listaCasas[i].mostrar_casa()
            i = i+1

    elif op ==4:
        i=0
        for vivienda in listaDepto:
            print("Departamentos : ")
            listaDepto[i].mostrar_departamento()
            i = i+1
        
    elif op == 0:
        print("Gracios por utilzar este programa")

    else:
        print("Ingrese una opcion valida")
        