import tkinter as tk
from tkinter import messagebox

# Base de datos de estudiantes (lista de diccionarios)
base_de_datos = []

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = entry_nombre.get()
    id = entry_id.get()
    edad = entry_edad.get()

    if not nombre or not id or not edad:
        messagebox.showwarning("Datos incompletos", "Por favor, rellene todos los campos.")
        return

    # Creamos un diccionario con los datos del estudiante
    estudiante = {"nombre": nombre, "id": int(id), "edad": int(edad)}

    # Lo agregamos a la base de datos
    base_de_datos.append(estudiante)
    messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
    limpiar_campos()

def mostrar_estudiantes():
    if base_de_datos:
        estudiantes = "\n".join([f"ID: {est['id']}, Nombre: {est['nombre']}, Edad: {est['edad']}" for est in base_de_datos])
        messagebox.showinfo("Lista de Estudiantes", estudiantes)
    else:
        messagebox.showinfo("Lista Vacía", "No hay estudiantes en la base de datos.")

def buscar_estudiante():
    id = entry_buscar_id.get()

    if not id:
        messagebox.showwarning("Falta ID", "Por favor, ingrese el ID del estudiante a buscar.")
        return

    for estudiante in base_de_datos:
        if estudiante["id"] == int(id):
            messagebox.showinfo("Estudiante Encontrado", f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
            return
    messagebox.showerror("No Encontrado", "Estudiante no encontrado.")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_buscar_id.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Estudiantes")

# Widgets de entrada y botones
label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_id = tk.Label(root, text="ID:")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

label_edad = tk.Label(root, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

btn_agregar = tk.Button(root, text="Agregar Estudiante", command=agregar_estudiante)
btn_agregar.pack()

label_buscar_id = tk.Label(root, text="Buscar Estudiante por ID:")
label_buscar_id.pack()
entry_buscar_id = tk.Entry(root)
entry_buscar_id.pack()

btn_buscar = tk.Button(root, text="Buscar", command=buscar_estudiante)
btn_buscar.pack()

btn_mostrar = tk.Button(root, text="Mostrar Estudiantes", command=mostrar_estudiantes)
btn_mostrar.pack()

btn_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.pack()

# Ejecutar el bucle principal de la ventana
root.mainloop()
