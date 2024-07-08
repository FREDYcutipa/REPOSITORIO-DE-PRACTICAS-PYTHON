"""Escribir un programa que cree un diccionario simulando un carrito de compra. El 
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que 
el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
y el costo total, con el siguiente formato:
ARTICULO 1 PRECIO.
ARTICULO 2 PRECIO.
ARTICULO 3 PRECIO.
.................
TOTAL:     COSTO """
carrito = {}
continuar = True

while continuar:
    articulo = input("Introduce el nombre del artículo (o 'T' para finalizar): ")
    if articulo.lower() == "t":
        continuar = False
    else:
        precio = float(input(f"Introduce el precio de '{articulo}': "))
        carrito[articulo] = precio

print("\nLista de la compra:")
total = 0  

for articulo, precio in carrito.items():
    linea = f"{articulo}: {precio} soles" 
    print(linea)
    total += precio  

print("\nTOTAL:", total, "soles") 
