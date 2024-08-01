import mariadb
import sys
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ESTA PARTE CONECTA CON LA BASE DE DATOS MARIABD
try:
    conn = mariadb.connect(
        user="root",
        password="",  
        host="127.0.0.1",
        port=3307,
        database="sistema_matricula"
    )
    c = conn.cursor()
except mariadb.Error as e:
    print(f"Error al conectar con la plataforma MariaDB: {e}")
    sys.exit(1)
    
def ajustar_imagen(ruta, tamaño):
    imagen = Image.open(ruta)
    imagen = imagen.resize(tamaño)
    return ImageTk.PhotoImage(imagen)

def actualizar_imagen_carrera(*args):
    carrera = carrera_var.get()
    if carrera == "Computación e Informática":
        nueva_imagen = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/I_COMP.png", (300, 300))
    elif carrera == "Producción Agropecuaria":
        nueva_imagen = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/I_AGRO.png", (300, 300))
    elif carrera == "Enfermería Técnica":
        nueva_imagen = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/I_ENFE.png", (300, 300))
    else:
        return

    label_imagen_carrera.configure(image=nueva_imagen)
    label_imagen_carrera.image = nueva_imagen
    
# Lista global para almacenar los registros
registros = []

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    usuarios_permitidos = ["FREDY", "SYDNAY", "OSCAR", "YUDI"]
    if usuario.upper() in usuarios_permitidos and contrasena == "admin":
        ocultar_login()
        mostrar_bienvenida(usuario)
    else:
        mostrar_error("Usuario o contraseña incorrectos")

def ocultar_login():
    frame_login.place_forget()

def mostrar_bienvenida(usuario):
    bienvenida_label = Label(Ventana, text=f"Bienvenido administrador (a), {usuario}!", font=("Arial", 16, "bold"), fg="green", bg="yellow")
    bienvenida_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    Ventana.after(3000, (lambda: [bienvenida_label.destroy(), mostrar_registro()]))

def mostrar_error(mensaje):
    global error_label
    error_label = Label(Ventana, text=mensaje, font=("Arial", 12, "bold"), fg="red", bg="white")
    error_label.place(relx=0.5, rely=0.75, anchor=CENTER)
    Ventana.after(3000, error_label.destroy)

def mostrar_registro():
    global frame_registro
    frame_registro = Frame(Ventana, bg="lightblue", bd=2, relief=SOLID)
    frame_registro.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=150)

    Label(frame_registro, text="REGISTRO DE MATRÍCULAS", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    boton_nuevo = Button(frame_registro, text="Nuevo Registro", font=("Arial", 12), command=mostrar_formulario)
    boton_nuevo.pack(side=LEFT, padx=20)

    boton_general = Button(frame_registro, text="Registro General de Matriculados", font=("Arial", 12), command=mostrar_registro_general)
    boton_general.pack(side=LEFT, padx=20)

    boton_volver = Button(frame_registro, text="Volver", font=("Arial", 12), command=volver_a_login)
    boton_volver.pack(side=RIGHT, padx=20)
    
#OSCAR/FREDY

def mostrar_formulario():
    global frame_formulario
    frame_formulario = Frame(Ventana, bg="lightgreen", bd=2, relief=SOLID)
    frame_formulario.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=400)

    Label(frame_formulario, text="Formulario de Matrícula", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=10)

    Label(frame_formulario, text="Apellidos:", font=("Arial", 12), bg="lightgreen").place(x=20, y=60)
    global entry_apellidos
    entry_apellidos = Entry(frame_formulario, font=("Arial", 12))
    entry_apellidos.place(x=150, y=60, width=400)

    Label(frame_formulario, text="Nombres:", font=("Arial", 12), bg="lightgreen").place(x=20, y=100)
    global entry_nombres
    entry_nombres = Entry(frame_formulario, font=("Arial", 12))
    entry_nombres.place(x=150, y=100, width=400)

    Label(frame_formulario, text="DNI:", font=("Arial", 12), bg="lightgreen").place(x=20, y=140)
    global entry_dni
    entry_dni = Entry(frame_formulario, font=("Arial", 12))
    entry_dni.place(x=150, y=140, width=400)

    Label(frame_formulario, text="Carrera Profesional:", font=("Arial", 12), bg="lightgreen").place(x=20, y=180)
    global carrera_var
    carrera_var = StringVar(value="Computación e Informática")
    opciones_carrera = ["Computación e Informática", "Producción Agropecuaria", "Enfermería Técnica"]
    carrera_menu = OptionMenu(frame_formulario, carrera_var, *opciones_carrera)
    carrera_menu.place(x=180, y=175)

    Label(frame_formulario, text="Periodo Académico:", font=("Arial", 12), bg="lightgreen").place(x=20, y=220)
    global periodo_var
    periodo_var = StringVar(value="2024")
    opciones_periodo = [f"{año} - {semestre}" for año in range(2024, 2027) for semestre in range(1, 3)]
    periodo_menu = OptionMenu(frame_formulario, periodo_var, *opciones_periodo)
    periodo_menu.place(x=180, y=215)

    Label(frame_formulario, text="Semestre:", font=("Arial", 12), bg="lightgreen").place(x=20, y=260)
    global semestre_var
    semestre_var = StringVar(value="1")
    semestre_menu = OptionMenu(frame_formulario, semestre_var, *[str(i) for i in range(1, 7)])
    semestre_menu.place(x=150, y=255)

    Label(frame_formulario, text="Plan Curricular:", font=("Arial", 12), bg="lightgreen").place(x=20, y=300)
    global plan_var
    plan_var = StringVar(value="Sistema Modular")
    plan_menu = OptionMenu(frame_formulario, plan_var, "Sistema Modular")
    plan_menu.place(x=150, y=295)

    boton_guardar = Button(frame_formulario, text="Guardar", font=("Arial", 12), command=guardar_registro)
    boton_guardar.place(x=200, y=350)

    boton_volver = Button(frame_formulario, text="Volver", font=("Arial", 12), command=volver_a_registro)
    boton_volver.place(x=280, y=350)
    
    global label_imagen_carrera
    label_imagen_carrera = Label(Ventana)
    label_imagen_carrera.place(relx=0.14, rely=0.5, anchor=CENTER)

    # Asociar la variable carrera_var con la función de actualización de imagen
    carrera_var.trace("w", actualizar_imagen_carrera)

"""
def guardar_registro():
    # Obtener datos del formulario
    apellidos = entry_apellidos.get()
    nombres = entry_nombres.get()
    dni = entry_dni.get()
    carrera = carrera_var.get()
    periodo = periodo_var.get()
    semestre = semestre_var.get()
    plan = plan_var.get()
    
    registros.append([apellidos, nombres, dni, carrera, periodo, semestre, plan])"""

    # Guardar en la base de datos en la tabla 'estudiantes'
def insertar_estudiante(apellidos, nombres, dni, carrera, periodo, semestre, plan):
    try:
        c.execute('''
            INSERT INTO estudiantes (apellidos, nombres, dni, carrera, periodo, semestre, plan)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',(apellidos, nombres, dni, carrera, periodo, semestre, plan))
        conn.commit()
        print("Registro insertado exitosamente.")
    except mariadb.Error as e:
        print(f"Error al insertar el registro: {e}")

# Función para obtener todos los estudiantes
def obtener_estudiantes():
    try:
        c.execute("SELECT * FROM estudiantes")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except mariadb.Error as e:
        print(f"Error al obtener registros: {e}")

    # Limpiar campos del formulario
    borrar_campos()

    # Limpiar campos del formulario
    borrar_campos()

def guardar_registro():
    apellidos = entry_apellidos.get()
    nombres = entry_nombres.get()
    dni = entry_dni.get()
    carrera = carrera_var.get()
    periodo = periodo_var.get()
    semestre = semestre_var.get()
    plan = plan_var.get()

    # Guardar en la base de datos
    insertar_estudiante(apellidos, nombres, dni, carrera, periodo, semestre, plan)

    mostrar_mensaje_exitoso()
    borrar_campos()

def borrar_campos():
    entrada_usuario.delete(0, END)
    entrada_contrasena.delete(0, END)


def mostrar_mensaje_exitoso():
    global mensaje_exitoso
    mensaje_exitoso = Toplevel(Ventana)
    mensaje_exitoso.title("Registro Exitoso")
    mensaje_exitoso.geometry("300x100+{}+{}".format(
        (Ventana.winfo_screenwidth() - 300) // 2,
        (Ventana.winfo_screenheight() - 100) // 2
    ))

    Label(mensaje_exitoso, text="¡Registro exitoso!", font=("Arial", 14, "bold"), fg="green").pack(pady=20)
    boton_aceptar = Button(mensaje_exitoso, text="Aceptar", command=mensaje_exitoso.destroy)
    boton_aceptar.pack(pady=10)

def mostrar_registro_general():
    global frame_registro_general
    frame_registro_general = Toplevel(Ventana)
    frame_registro_general.title("Registro General de Matriculados")
    frame_registro_general.geometry("800x400+{}+{}".format(
        (Ventana.winfo_screenwidth() - 800) // 2,
        (Ventana.winfo_screenheight() - 400) // 2
    ))

    tree = ttk.Treeview(frame_registro_general, columns=("Apellidos", "Nombres", "DNI", "Carrera Profesional", "Periodo Académico", "Semestre", "Plan Curricular"), show='headings')
    tree.pack(fill=BOTH, expand=1)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for registro in registros:
        tree.insert("", END, values=registro)
    
def volver_a_login():
    frame_registro.place_forget()
    frame_login.place(relx=0.5, rely=0.5, anchor=CENTER, width=ancho_frame, height=alto_frame)

def volver_a_registro():
    frame_formulario.place_forget()
    frame_registro.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=150)

Ventana = Tk()
Ventana.title("Sistema de Matrículas")
Ventana.attributes('-fullscreen', True)

# Cargar y ajustar imágenes
def ajustar_imagen(ruta, tamaño):
    imagen = Image.open(ruta)
    imagen = imagen.resize(tamaño)
    return ImageTk.PhotoImage(imagen)

photo1 = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/INSIGNIA.png", (100, 100))
photo2 = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/INSIGNIA.png", (100, 100))
photo3 = ajustar_imagen("E:/ING GRETLY/PROYECTO COMPLETO DE SISTEMA DE MATRICULAS/F_TECNO.png", (Ventana.winfo_screenwidth(), Ventana.winfo_screenheight()))

# Crear etiquetas para mostrar las imágenes
Label(Ventana, image=photo3).place(x=0, y=0, relwidth=1, relheight=1)
Label(Ventana, image=photo1).place(x=0, y=0)
Label(Ventana, image=photo2).place(x=Ventana.winfo_screenwidth() - 100, y=0)

texto = "INSTITUTO DE EDUCACIÓN SUPERIOR\nTECNOLÓGICO PÚBLICO DE ACORA"
Label(Ventana, text=texto, font=("Arial", 18, "bold"), fg="black", bg="red").place(relx=0.5, y=20, anchor=N)

ancho_frame = 300
alto_frame = 200

frame_login = Frame(Ventana, bg="yellow", bd=2, relief=SOLID)
frame_login.place(relx=0.5, rely=0.5, anchor=CENTER, width=ancho_frame, height=alto_frame)

Label(frame_login, text="Usuario:", font=("Arial", 12), bg="yellow").place(x=20, y=20)
entrada_usuario = Entry(frame_login, font=("Arial", 12))
entrada_usuario.place(x=100, y=20, width=180)

Label(frame_login, text="Password:", font=("Arial", 12), bg="yellow").place(x=20, y=70)
entrada_contrasena = Entry(frame_login, font=("Arial", 12), show="*")
entrada_contrasena.place(x=100, y=70, width=180)

Button(frame_login, text="Iniciar Sesión", font=("Arial", 12), command=iniciar_sesion).place(x=50, y=120)
Button(frame_login, text="Borrar", font=("Arial", 12), command=borrar_campos).place(x=200, y=120)

Ventana.mainloop()
