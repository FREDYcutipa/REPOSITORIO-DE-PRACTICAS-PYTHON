"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el 
número de factura y el valor el coste de la factura. El programa debe preguntar al 
usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea 
añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá 
al diccionario. Si se desea pagar una factura se preguntará por el número de factura y 
se eliminará del diccionario, y deberá añadir el 18% del monto a pagar. Después de 
cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el 
momento y la cantidad pendiente de cobro."""

facturas = {}
cobrado = 0
pendiente = 0
terminar = False

while not terminar:
    print("\nMenú de opciones:")
    print("1. Añadir nueva factura")
    print("2. Pagar factura existente")
    print("3. Terminar")

    opcion = input("Seleccione una opción (1), (2), (3): ")

    if opcion == "1": 
        numero_factura = input("Escriba el número de factura: ")
        precio_factura = float(input("Introduce el costo de la factura: "))
        facturas[numero_factura] = precio_factura
        pendiente += precio_factura

    elif opcion == "2":
        numero_factura = input("Escriba el número de factura a pagar: ")
        if numero_factura in facturas:
            precio_factura = facturas.pop(numero_factura)
            IVA = precio_factura * 0.18
            cobrado += precio_factura + IVA
            pendiente -= precio_factura
            print(f"Se canceló la factura {numero_factura}. Se añadió el 18% de IVA: ${IVA}")
        else:
            print(f"No existe una factura con ese número {numero_factura}")
            
    elif opcion == "3":
        terminar = True
    else:
        print("Opción no válida. Inténtelo de nuevo.")
    print(f"\nEl monto cobrado hasta ahora es: ${cobrado}")
    print(f"El monto que falta cobrar es: ${pendiente}")

