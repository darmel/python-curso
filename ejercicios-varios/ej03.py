'''3) Escribir un algoritmo que convierta temperaturas de
Fahrenheit a Celcius. Utilizar la fórmula ºC = (5/9)·(ºF – 32).'''


temp_f = int(input('ingrese una temperatura en °F: '))
temp_c = round((5/9)*(temp_f-32))

print(' la temperatura es equivalente a: ', temp_c)
