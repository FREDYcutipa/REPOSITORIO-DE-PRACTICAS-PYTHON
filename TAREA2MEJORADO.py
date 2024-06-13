# agregamos datos basicos
CAT5 = 24
CAT6 = 20
ROUTER = 125

# multiplicamos el precio por metro de cada cable por el costo de cada cable.
PPMCAT5 = CAT5 * 3.50
PPMCAT6 = CAT6 * 4.80

# muestra los rsultados de la mutiplicacion
print("Precio OP1 de cat5:", PPMCAT5)
print("Precio OP2 de cat6:", PPMCAT6)

# antes de esto dividimos el IGV 18% entre 100 y tendremos un resultado de 0.18/0.16 y eso lo multiplicamos.
OPCION1 = PPMCAT5 * 0.18
OPCION2 = PPMCAT6 * 0.16

# muestra el precio or categoria.
print("precio OP1 de cat5 con IGV:", OPCION1)
print("precio OP2 de cat6 con IGV:", OPCION2)

# sumarle el precio de los router a cada categoria
PARACAT5 = ROUTER * 3
PARACAT6 = ROUTER * 5

# muestra el precio de los routers
print("el precio de los routers para CAT5:", PARACAT5)
print("el precio de los routers para CAT6:", PARACAT6)

#ahora sumamos cada una delas opciones con su respectiva precio de router.
PT_OPCION1 = OPCION1 + PARACAT5
PT_OPCION2 = OPCION2 + PARACAT6

# muestra el total de los precios de cada OPCION.
print("PRECIO TOTAL DE COMPRA PARA OPCION 1:", PT_OPCION1)
print("PRECIO TOTAL DE COMPRA PARA OPCION 2:", PT_OPCION2)

# sumamos las dos opciones para sacar un presupuesto general.
TOTAL = PT_OPCION1 + PT_OPCION2

# muestra el resulatdo general
print("RESULTADO GENERAL:", TOTAL)
