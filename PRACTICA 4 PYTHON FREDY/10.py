X = int(input("INGRESE CUALQUIER NUMERO ENTERO: "))
INICIAR_DESDE = 1

while INICIAR_DESDE <= X:  
   
    numero_act = INICIAR_DESDE
       
    while numero_act >= 1 :
        print(numero_act, end=' ')
        numero_act -= 2  
    print()  
    INICIAR_DESDE += 2  
