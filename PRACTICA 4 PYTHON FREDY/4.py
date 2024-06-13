
NOMBRE = input("Ingrese su nombre: ")
SEXO = input("Ingrese su sexo (Mujer/Hombre): ")

if SEXO == "MUJER":
    if NOMBRE.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if NOMBRE.lower() < "n":
        grupo = "A"
    else:
        grupo = "B"
print("PERTENECES AL GRUPO: " + grupo , "FELICITACIONES")