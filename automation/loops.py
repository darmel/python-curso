frutas = ["manzana", "naranja", "peras", "frutilla", "uva"]

for i in frutas:
    print("would yo like {} ? ".format(i))

for number in range(1, 11):  # el ultimo no esta incluido
    print("number {}".format(number))

# WHILE

temp_c = 40
while temp_c > 0:
    print("The water is {} degrees".format(temp_c))
    temp_c -= 1
    if temp_c == 33:
        break

# BREAK: sale del loop
# Continue: salta la parte del loop
# pass: pasa la parte del loop

for number in range(1, 11):
    if number == 7:
        print("we are skiiping number 7")
        continue
    if number == 3:
        pass
    else:
        print("This is the number {}".format(number))

on = True


def suma():
    a = float(input("enter a number: "))
    b = float(input("enter another numberr"))
    print(a+b)


def resta():
    a = float(input("enter a number: "))
    b = float(input("enter another number: "))
    print(a-b)


def multiplicacion():
    a = float(input("enter a number: "))
    b = float(input("enter another number: "))
    print(a*b)


def division():
    a = float(input("enter a number: "))
    b = float(input("enter another number: "))
    print(a/b)


while on:
    operacion = input("please type +, -, * or / ")
    if operacion == '+':
        suma()
    elif operacion == '-':
        resta()
    elif operacion == '*':
        multiplicacion()
    elif operacion == '/':
        division()
    elif operacion == 'q':
        on = False
    else:
        print("operacion no soportada")
