# Escribir un programa que almacene los cursos HDS, AG, DG, TPC, TPO en una lista, 
# pregunte al ususario la nota que sacado en cada curso y elimine de la lista 
# los cursos que ha aprovado y imprima por pantalla los cursos que el usurio a reprobado. 

def NOTAS(cursos):
    aprobado = []
    for curso in cursos[:]: 
        nota = float(input(f"Ingrese su nota para {curso}: "))
        if nota >= 13:
            aprobado.append(curso)
            cursos.remove(curso) 
    return cursos

def APROBADOS(cursos):
    if len(cursos) == 0:
        print("Felicidades, Aprobó todos los cursos.")
    else:
        print("Usted ha reprobado los siguientes cursos:")
        for curso in cursos:
            print(curso)

cursos = ["HDS", "AG", "DG", "TPC", "TPO"]
cursos_reprobados = NOTAS(cursos[:]) 
APROBADOS(cursos_reprobados)
