EDAD_DEL_CLIENTE= input("ingrese su edad: ")
EDAD = int(EDAD_DEL_CLIENTE)
        
if EDAD < 4:
    precio = 0  
elif 4 <= EDAD <= 18:
    precio = 10
else:
    precio = 20  
     
print("El precio de la entrada es: ", precio , " soles.")
