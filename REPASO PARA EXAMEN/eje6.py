"""escribir un programa que permita gestionar la base de datos de clientes de una empresa, los clientes se guardadran en un diccionario
en el que la clave de cada cliente será su NIF y el valor será otro diccionario con los datos del cliente (nombre,direccion,
celular,correo, preferente),donde preferente tendrá el valor true si se trata de un cliente preferente. el programa debe pregunatar
al usuario por una opcion del: siguiente menú (1)añadir cliente, (2)eliminar cliente, (3) mostrar cliente,(4)listar todos los clientes
(5) listar clientes preferentes, (6)terminar en funsion de la opcion elegida el programa tendrá que hacer lo siguiente:

preguntar los datos del cliente, crear un diccionario con los datos y añadir a la base de datos.
preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
preguntar por el DNI del cliente y mostrar sus datos.
mostrar lista e todos los clientes con sus DNI y sombre.
mostrar la lista sde clientes preferentes de la base de datos con su DNI y nombre.
terminar el programa."""

clientes = {}
opcion = ""
while opcion != "6":
    if opcion == "1":
        dni = input("Introduce el DNI del cliente: ")
        nombre = input ("Escriba el nombre del cliente: ")
        direccion = input("Escriba la direccion del cliente: ")
        celular = input("Introdusca el numero de celular del cliente: ")
        email = input("Escriba el correo electronico del cliente: ")
        vip = input("¿es un cliente preferente? S/N: ")
        cliente = {"nombre " :nombre, "direccion: ":direccion,"telefono" :celular, "email:" :email, "preferente":vip }
        clientes[dni] = cliente
    if opcion == "2":
        dni = input ("introduce el DNI del cliente: ")
        if dni in clientes:
            del clientes[dni]
        else:
            print("no existe un cliente con el DNI: ", dni) 
    if opcion =="3":
        dni = input("introduce el DNI del cliente: ") 
        if dni in clientes:
            print ("DNI: ", dni) 
            for clave, valor in clientes[dni].items():
                print(clave.title() + ":", valor)
        else:
            print("no existe un cliente con el DNI: ", dni) 
    if opcion =="4":
        print("lista de todos los clientes: ")
        for clave, valor in clientes.items():
            print(clave,valor["nombre"])
    if opcion =="5":
        print("lista de clientes preferentes: ")
        for clave, valor in clientes.items():
            if valor["preferntes"]:
                print(clave,valor["nombre"])
    opcion = input ("menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) mostrar clientes\n(4) enlistar clienetes\n(5) clientes preferentes\n(6) Terminar" "\nELIGE UNA OPCION: ")            