#Escribir un programa que almacene los cursos HDS, AG, DG, TPC, TPO en una lista, 
# pregunte al ususario la nota que sacado en cada curso y elimine de la lista 
# los cursos que ha aprovado y imprima por pantalla los cursos que el usurio a reprobado. 

cursos = ["HDS", "AG", "DG", "TPC", "TPO"]
aprobado = []
for curso in cursos:
    nota = float(input("ingrese su nota " + curso + ": "))
    if nota >= 13:
        aprobado.append(curso)
for curso in aprobado:
    cursos.remove(curso) 
print("Usted a reprobado " + str(cursos))       
 
