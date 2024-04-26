print(1<1)
print(1<=1)

"""name = input("what is your name? ")
if name == "Dario":
    print("hello, nice to see you {}".format(name))
elif name=="Jose":
    print("hi, {}, you are a great person!".format(name))
elif name == "Martin":
    print("hi, {}, lets have lunch soon".format(name))
else:
    print("have a good day {}".format(name))
print("have a nice day!")
"""

def suma():
    a= float(input("enter a number: "))
    b = float(input("enter another numberr"))
    print(a+b)

def resta():
    a = float(input("enter a number: "))
    b= float(input("enter another number: "))
    print(a-b)


def multiplicacion():
    a = float(input("enter a number: "))
    b= float(input("enter another number: "))
    print(a*b)

def division():
    a = float(input("enter a number: "))
    b= float(input("enter another number: "))
    print(a/b)

operacion =input("please type +, -, * or / ")
if operacion== '+':
    suma()
elif operacion=='-':
    resta()
elif operacion=='*':
    multiplicacion()
elif operacion=='/':
    division()
else:
    print("operacion no soportada")

