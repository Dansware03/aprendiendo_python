import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexión a la base de datos SQLite
conexion = sqlite3.connect('bd_estudiantes.db')
cursor = conexion.cursor()

# Crear tabla de estudiantes si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')
conexion.commit()

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = entry_nombre.get()
    id = entry_id.get()
    edad = entry_edad.get()

    if not nombre or not id or not edad:
        messagebox.showwarning("Datos incompletos", "Por favor, rellene todos los campos.")
        return

    try:
        # Insertar en la base de datos
        cursor.execute("INSERT INTO estudiantes (id, nombre, edad) VALUES (?, ?, ?)", (int(id), nombre, int(edad)))
        conexion.commit()
        messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
        limpiar_campos()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El ID ya existe en la base de datos.")

def mostrar_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    if estudiantes:
        estudiantes_str = "\n".join([f"ID: {est[0]}, Nombre: {est[1]}, Edad: {est[2]}" for est in estudiantes])
        messagebox.showinfo("Lista de Estudiantes", estudiantes_str)
    else:
        messagebox.showinfo("Lista Vacía", "No hay estudiantes en la base de datos.")

def buscar_estudiante():
    id = entry_buscar_id.get()

    if not id:
        messagebox.showwarning("Falta ID", "Por favor, ingrese el ID del estudiante a buscar.")
        return

    cursor.execute("SELECT * FROM estudiantes WHERE id = ?", (int(id),))
    estudiante = cursor.fetchone()

    if estudiante:
        messagebox.showinfo("Estudiante Encontrado", f"Nombre: {estudiante[1]}, Edad: {estudiante[2]}")
    else:
        messagebox.showerror("No Encontrado", "Estudiante no encontrado.")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_buscar_id.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Estudiantes")
root.geometry("450x450")
root.configure(bg="#f8f9fa")

# Estilo de Bootstrap con colores
PRIMARY_COLOR = "#0d6efd"
SUCCESS_COLOR = "#198754"
DANGER_COLOR = "#dc3545"
LIGHT_COLOR = "#f8f9fa"
DARK_COLOR = "#343a40"
FONT_COLOR_LIGHT = "white"

# Frames para separar las secciones
frame_agregar = tk.Frame(root, padx=10, pady=10, bg=LIGHT_COLOR, relief=tk.SOLID, bd=1)
frame_agregar.pack(pady=10, padx=10, fill="both", expand=True)

frame_buscar = tk.Frame(root, padx=10, pady=10, bg=LIGHT_COLOR, relief=tk.SOLID, bd=1)
frame_buscar.pack(pady=10, padx=10, fill="both", expand=True)

# Widgets de entrada para agregar estudiante
label_titulo_agregar = tk.Label(frame_agregar, text="Agregar Estudiante", bg=LIGHT_COLOR, font=('Helvetica', 16, 'bold'), fg=DARK_COLOR)
label_titulo_agregar.grid(row=0, columnspan=2, pady=10)

label_nombre = tk.Label(frame_agregar, text="Nombre:", bg=LIGHT_COLOR)
label_nombre.grid(row=1, column=0, pady=5, padx=5, sticky="e")
entry_nombre = tk.Entry(frame_agregar, highlightbackground=PRIMARY_COLOR)
entry_nombre.grid(row=1, column=1, pady=5)

label_id = tk.Label(frame_agregar, text="ID:", bg=LIGHT_COLOR)
label_id.grid(row=2, column=0, pady=5, padx=5, sticky="e")
entry_id = tk.Entry(frame_agregar, highlightbackground=PRIMARY_COLOR)
entry_id.grid(row=2, column=1, pady=5)

label_edad = tk.Label(frame_agregar, text="Edad:", bg=LIGHT_COLOR)
label_edad.grid(row=3, column=0, pady=5, padx=5, sticky="e")
entry_edad = tk.Entry(frame_agregar, highlightbackground=PRIMARY_COLOR)
entry_edad.grid(row=3, column=1, pady=5)

btn_agregar = tk.Button(frame_agregar, text="Agregar Estudiante", command=agregar_estudiante, bg=SUCCESS_COLOR, fg=FONT_COLOR_LIGHT)
btn_agregar.grid(row=4, columnspan=2, pady=10, ipadx=20)

# Widgets para buscar estudiante
label_titulo_buscar = tk.Label(frame_buscar, text="Buscar Estudiante", bg=LIGHT_COLOR, font=('Helvetica', 16, 'bold'), fg=DARK_COLOR)
label_titulo_buscar.grid(row=0, columnspan=2, pady=10)

label_buscar_id = tk.Label(frame_buscar, text="Buscar por ID:", bg=LIGHT_COLOR)
label_buscar_id.grid(row=1, column=0, pady=5, padx=5, sticky="e")
entry_buscar_id = tk.Entry(frame_buscar, highlightbackground=PRIMARY_COLOR)
entry_buscar_id.grid(row=1, column=1, pady=5)

btn_buscar = tk.Button(frame_buscar, text="Buscar", command=buscar_estudiante, bg=PRIMARY_COLOR, fg=FONT_COLOR_LIGHT)
btn_buscar.grid(row=2, columnspan=2, pady=10, ipadx=20)

# Botones adicionales
btn_mostrar = tk.Button(root, text="Mostrar Estudiantes", command=mostrar_estudiantes, bg=SUCCESS_COLOR, fg=FONT_COLOR_LIGHT)
btn_mostrar.pack(pady=10, ipadx=30)

btn_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos, bg=DANGER_COLOR, fg=FONT_COLOR_LIGHT)
btn_limpiar.pack(pady=5, ipadx=40)

# Ejecutar el bucle principal de la ventana
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()
