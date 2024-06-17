Ncursos = [ "HDS", "AG", "DG", "TPW", "PC"]
NOTAS = {}
for curso in Ncursos:
    nota = input (f"INTRODUCE LA NOTA{curso}:")
    NOTAS[curso]= nota
print("\n LAS NOTAS SON: ")
for curso, nota in NOTAS.items():
    print (f"en{curso}SU NOTA ES:{nota}")
    