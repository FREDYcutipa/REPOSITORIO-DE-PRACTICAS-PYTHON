
FRASE = input("INGRESE SU FRASE: ")
LETRA = input("INGRESE CUALQUIER LETRA QUE TENGA LA FRASE: ")

contador = 0
indice = 0
while indice < len(FRASE):
     
    if FRASE[indice] == LETRA:
        contador += 1  
       
    indice += 1

print(f"La letra '{LETRA}' aparece {contador} veces en la frase.")