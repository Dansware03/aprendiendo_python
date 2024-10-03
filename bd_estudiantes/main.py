# Base de datos de estudiantes (lista de diccionarios)
base_de_datos = []

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    id = int(input("Ingrese el número de identificación: "))
    edad = int(input("Ingrese la edad del estudiante: "))

    # Creamos un diccionario con los datos del estudiante
    estudiante = {"nombre": nombre, "id": id, "edad": edad}

    # Lo agregamos a la base de datos
    base_de_datos.append(estudiante)
    print("Estudiante agregado correctamente.\n")

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    if base_de_datos:
        print("Lista de estudiantes:")
        for estudiante in base_de_datos:
            print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
    else:
        print("La base de datos está vacía.\n")

# Función para buscar un estudiante por ID
def buscar_estudiante():
    id = int(input("Ingrese el ID del estudiante que desea buscar: "))
    for estudiante in base_de_datos:
        if estudiante["id"] == id:
            print(f"Estudiante encontrado: Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
            return
    print("Estudiante no encontrado.\n")

# Función para actualizar la información de un estudiante
def actualizar_estudiante():
    id = int(input("Ingrese el ID del estudiante que desea actualizar: "))
    for estudiante in base_de_datos:
        if estudiante["id"] == id:
            nombre = input(f"Ingrese el nuevo nombre (actual: {estudiante['nombre']}): ")
            edad = int(input(f"Ingrese la nueva edad (actual: {estudiante['edad']}): "))
            estudiante["nombre"] = nombre
            estudiante["edad"] = edad
            print("Información del estudiante actualizada.\n")
            return
    print("Estudiante no encontrado.\n")

# Función para eliminar un estudiante
def eliminar_estudiante():
    id = int(input("Ingrese el ID del estudiante que desea eliminar: "))
    for estudiante in base_de_datos:
        if estudiante["id"] == id:
            base_de_datos.remove(estudiante)
            print("Estudiante eliminado correctamente.\n")
            return
    print("Estudiante no encontrado.\n")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Base de Datos de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante por ID")
        print("4. Actualizar información de estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

# Ejecutar el menú
menu()
