#determine la nota final de un estudiante cosiderando lo siguiente
#nota de practica =50%
#notas de examen =30%.
#nota de tareas = 20%.

# INGRESANDO LAS NOTAS
nota_practica = float(input("Ingrese la nota de PRACTICA: "))
nota_examen = float(input("Ingrese la nota de EXAMEN: "))
nota_tareas = float(input("Ingrese la nota de TAREA: "))
print(nota_practica,nota_examen,nota_tareas)

# Calcula la nota final
nota_final = (nota_practica * 0.5) + (nota_examen * 0.3) + (nota_tareas * 0.2)

print("La nota final del estudiante es:", nota_final)