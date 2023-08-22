import tkinter as tk
import clases as c
import sql_functions as sql

sql.conectar_sql()

app = tk.Tk()

# Variables para manejo de forms
nombre = tk.StringVar()
apellido = tk.StringVar()
edad = tk.StringVar()

# Funciones de la App

def guardar_persona_en_db(persona_a_guardar):
    sql.crear_persona(persona_a_guardar)
    
    # Borro los forms
    nombre.set("")
    apellido.set("")
    edad.set("")


def crear_persona(nombre, apellido, edad):
    if(nombre != "" and apellido != "" and edad != ""):
        nueva_persona = c.Persona(nombre,apellido,edad)
        
        guardar_persona_en_db(nueva_persona)
        
def ver_personas():
    pass
        

app.title("Mi primera aplicación")
app.geometry("800x500")

label = tk.Label(app,
                 text="Parcial de Paradigmas de Programación",
                 font=("Arial Bold", 20)
                 ).pack(
    fill=tk.X,
)

# Formulario para el nombre: 

label = tk.Label(app,
                 text="Ingrese su nombre:",
                 font=("Arial Bold", 15)
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)

entry = tk.Entry(app,
                 font=("Arial Bold", 15),
                 textvariable=nombre
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)
                 
                 
# Formulario para el apellido: 

label = tk.Label(app,
                 text="Ingrese su apellido:",
                 font=("Arial Bold", 15),
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)

entry = tk.Entry(app,
                 font=("Arial Bold", 15),
                 textvariable=apellido
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)

# Formulario para la edad
label = tk.Label(app,
                 text="Ingrese su edad:",
                 font=("Arial Bold", 15)
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)

entry = tk.Entry(app,
                 font=("Arial Bold", 15),
                 textvariable=edad
                 ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)

# Boton para enviar los datos
button = tk.Button(app,
                   text="Enviar datos para crear persona",
                   font=("Arial Bold", 15),
                   command=lambda: crear_persona(nombre.get(),apellido.get(),edad.get())
                   ).pack(
    fill=tk.X,
    padx=10,
    pady=10,
)
                   
                   
button = tk.Button(app,
                   text="Ver las personas creadas",
                   font=("Arial Bold", 15),
                   command=lambda: ver_personas()
                ).pack(
                    padx=20,
                    pady=20
                )

tk.mainloop()
