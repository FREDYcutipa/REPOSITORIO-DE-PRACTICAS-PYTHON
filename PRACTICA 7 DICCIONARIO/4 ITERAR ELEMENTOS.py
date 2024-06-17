# ITERAR ELEMENTOS
print (" primer metodo")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
for clave in ESTUDIANTES:
    print(clave, ESTUDIANTES[clave])

print ("segundo metodo")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
for clave, valor in ESTUDIANTES.items():
    print(clave, valor)
