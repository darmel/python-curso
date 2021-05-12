#ciclo for
'''estructura de repeticion
se necesita: 
Inicio
Fin,
Incremento:
'''
sum = 0
for i in range(0,3,1): #(inicio, fin, incremento)
    num = int(input('ingrese un número: '))
    sum = sum + num

print(f'la suma es: {sum}')

#ciclo for en vectores
frutas = ['manzana','pera','anana',12,'uva']

for i in frutas:
    print(i)

#ciclo while
'''el ciclo whilerepite las instruciones mientras se cumpla la condicion
no se sabe cuantas veces se repite'''

temp = int(input("ingrese la temperatura del agua: "))
while temp > 0 :
    print('el agua no esta congelada, se encuetra a: ', temp, '°C')
    temp = temp -1

print('el agua esta congelada')