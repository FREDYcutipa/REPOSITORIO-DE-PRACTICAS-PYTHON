""" Escribir un programa que gestione las facturas pendientes de cobro de una empresa. las facturas se almacenaran 
en diccionario donde la clave de cada factura srá el numero de factura y el valor el coste de la factura. 
el programa debepreguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar
si desea añadir una nueva factura se preguntará por el numero de factura y su coste y se añadiá al diccionario.
si se decea pagar una factura se preguntaá por el numero de factura y se eliminará del diccionario.
despues de cada operacion el programa debe mostrar por pantalla lka cantidad cobrada hasta el momento y la cantidad pendiente de cobrar."""
facturas = {}
cobrado =  0
pendiente = 0
sumando = ""
while sumando != "T":
    if sumando == "A":
        clave = input("introduce el numero de la factura: ")
        valor_1 = float(input("introduce el monto de la factura: "))
        facturas[clave]= valor_1
        pendiente += valor_1
    if sumando == "P":
        clave = input("introduce el numero de la factura a pagar: ")
        valor_1 = facturas.pop(clave, 0)
        cobrado += valor_1
        pendiente -= valor_1
    print ("Recaudado: ", cobrado)
    print ("pedniente de cobro: ", pendiente)
    sumando = input("¿quieres añadir una nueva factura (A), pargar (P), o terminar (T)? ")      
      
        
    