# Escribir una funsion que convierta un numero decimal en BINARIO y otra que convierta un numero BINARIO en decimal
def DECIMAL_A_BINARIO(decimal):
    ENTERA = int(decimal)
    BINARIO_INT = ""
    
    if ENTERA == 0:
        BINARIO_INT = "0"
    else:
        while ENTERA > 0:
            resto = ENTERA % 2
            BINARIO_INT = str(resto) + BINARIO_INT
            ENTERA = ENTERA // 2
    part_fraccion = decimal - int(decimal)
    bin_fraccion = ""
    
    if part_fraccion > 0:
        bin_fraccion = "."
        while part_fraccion > 0:
            part_fraccion *= 2
            BIT = int(part_fraccion)
            bin_fraccion += str(BIT)
            part_fraccion -= BIT
    
    return BINARIO_INT + bin_fraccion

def BINARIO_A_DECIMAL(BINARIO):
    
    if "." in BINARIO:
        ENTERA, part_fraccion = BINARIO.split(".")
    else:
        ENTERA = BINARIO
        part_fraccion = ""
    decimal_entero = 0
    for i, digito in enumerate(reversed(ENTERA)):
        if digito == "1":
            decimal_entero += 2 ** i
    decimal_fraccionario = 0
    for i, digito in enumerate(part_fraccion):
        if digito == "1":
            decimal_fraccionario += 2 ** -(i + 1)   
    return decimal_entero + decimal_fraccionario

NUM_DECIMAL = float(input("INTRODUCE TU NUMERO ENTERO O DECIMAL: "))

BINARIO = DECIMAL_A_BINARIO(NUM_DECIMAL)
print("EL NUMERO ", NUM_DECIMAL, " EN SU FORMA BINARIA ES: ", BINARIO)

RESULTADO_DECIMAL = BINARIO_A_DECIMAL(BINARIO)
print("EL NUMERO ", BINARIO, " EN FORMA DECIAML ES: ", RESULTADO_DECIMAL)


