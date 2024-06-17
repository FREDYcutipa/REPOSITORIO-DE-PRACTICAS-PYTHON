#ACCEDER A ELEMENTOS
print ("este es de forma 1")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
print(ESTUDIANTES["Ana"]) # 18

print ("este es de forma 2")

ESTUDIANTES = {"Juanito": 16, "Ana": 18, "Oscar": 17}
print(ESTUDIANTES.get("Maria", "No existe")) # "No existe"