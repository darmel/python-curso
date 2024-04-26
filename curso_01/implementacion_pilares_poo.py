from pilares_poo_08 import Alumno, Profesor

alumno = Alumno('Santiago', 'Passalacqua', 1)
alumno.mostrar()

alumno2 = Alumno('Juan', 'Perez', 3)
alumno2.mostrar()

#print(f'el apellido del alumno es {alumno2.apellido}')
alumno2.set_apellido("Gonzalez")
print("el apellido es", alumno2.apellido)

profesor = Profesor('Susana', 'Garcia', 32)
profesor.mostrar()