#AGREGAR Y MODIFICAR

print ("ESTE es de otra forma caso 1")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
ESTUDIANTES["Maria"] = 15
print(ESTUDIANTES) # {"Juanito": 16, "Ana": 18, "Oscar": 17, "Maria": 15}

print ("ESTE es de otra forma caso 2")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
ESTUDIANTES["Ana"] = 19
print(ESTUDIANTES) # {"Juanito": 16, "Ana": 19, "Oscar": 17}

print ("ESTE es de otra forma caso 3")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
del ESTUDIANTES["Juanito"]
print(ESTUDIANTES) # {"Ana": 18, "Oscar": 17}