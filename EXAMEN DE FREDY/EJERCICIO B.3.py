"""Escribir un programa que almacene los cursos HDS, AG, DG, TPC, TPD en una lista, 
pregunte al usuario la nota que ha sacado en cada curso y elimine de la lista los cursos 
desaprobados. Al final el programa debe mostrar por pantalla los cursos que el usuario 
a aprobado. """

cursos = ["HDS", "AG", "DG", "TPC", "TPD"]
cursos_aprobados = []
for curso in cursos:
    nota = float(input("Introduce la nota obtenida en " + curso + ": "))
    if nota >= 13:
       cursos_aprobados.append((curso, nota))
print("FELICITACIONES, Has aprobado los siguientes cursos:")
for curso, nota in cursos_aprobados:
    print(curso + " con la nota de: " + str(nota))