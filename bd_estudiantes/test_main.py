import pytest
import sqlite3

# Conectar con la base de datos de prueba
conexion = sqlite3.connect('bd_estudiantes_test.db')
cursor = conexion.cursor()

# Crear tabla de estudiantes si no existe (para la base de datos de prueba)
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')
conexion.commit()

# Función de utilidad para limpiar la base de datos antes de cada prueba
def limpiar_bd():
    cursor.execute("DELETE FROM estudiantes")
    conexion.commit()

# Prueba para agregar estudiante
def test_agregar_estudiante():
    limpiar_bd()  # Limpiar la base de datos antes de la prueba
    cursor.execute("INSERT INTO estudiantes (id, nombre, edad) VALUES (?, ?, ?)", (1, 'Juan', 20))
    conexion.commit()

    cursor.execute("SELECT * FROM estudiantes WHERE id = 1")
    estudiante = cursor.fetchone()

    assert estudiante is not None  # Comprobar que el estudiante fue agregado
    assert estudiante[1] == 'Juan'
    assert estudiante[0] == 1
    assert estudiante[2] == 20

# Prueba para mostrar estudiantes
def test_mostrar_estudiantes():
    limpiar_bd()  # Limpiar la base de datos antes de la prueba
    cursor.execute("INSERT INTO estudiantes (id, nombre, edad) VALUES (?, ?, ?)", (2, 'Ana', 22))
    conexion.commit()

    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    assert len(estudiantes) == 1  # Comprobar que hay un estudiante

# Prueba para buscar estudiante
def test_buscar_estudiante():
    limpiar_bd()  # Limpiar la base de datos antes de la prueba
    cursor.execute("INSERT INTO estudiantes (id, nombre, edad) VALUES (?, ?, ?)", (3, 'Carlos', 23))
    conexion.commit()

    cursor.execute("SELECT * FROM estudiantes WHERE id = 3")
    estudiante = cursor.fetchone()

    assert estudiante is not None  # Comprobar que el estudiante fue encontrado
    assert estudiante[1] == 'Carlos'
    assert estudiante[2] == 23

# Cerrar conexión al final de todas las pruebas
@pytest.fixture(scope="module", autouse=True)
def teardown_module():
    yield
    conexion.close()
