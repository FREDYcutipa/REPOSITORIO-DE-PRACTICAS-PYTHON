# agregamos datos basicos
CAT5 = 24
CAT6 = 20

# multiplicamos el precio por metro de cada cable por el costo de cada cable.
PPMCAT5 = CAT5 * 3.50
PPMCAT6 = CAT6 * 4.80

# muestra los rsultados de la mutiplicacion
print("costo de cat5:", PPMCAT5)
print("costo de cat6:", PPMCAT6)

# antes de esto dividimos el igv 18% entre 100 y tendremos un resultado de 0.18. y eso lo multiplicamos.
PRECIO1 = PPMCAT5 * 0.18
PRECIO2 = PPMCAT6 * 0.18

# muestra el precio or categoria.
print("precio cat5:",PRECIO1)
print("precio cat6:",PRECIO2)

# al final sumamos el precio uno con el precio dos y lo imprimimos.
TOTAL = PRECIO1 + PRECIO2
print("EL PRECIO TOTAL ES:", TOTAL)