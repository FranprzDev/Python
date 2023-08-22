import sqlite3
import os

def conecction_sql():
    # Obtiene la ruta absoluta del directorio actual
    directorio_actual = os.getcwd()
    print(directorio_actual)
    # Concatena el nombre de la base de datos al final de la ruta
    ruta_base_datos = os.path.join(directorio_actual, 'professor.db')
    
    conn = sqlite3.connect(ruta_base_datos)
    cursor = conn.cursor()
    
    query = """CREATE TABLE IF NOT EXISTS profesores 
    (id INTEGER PRIMARY KEY, 
     nombre TEXT,
     apellido TEXT,
     edad INTEGER,
     materia TEXT,
     antiguedadAnios INTEGER,
     comisiones TEXT
    )
    
    """

    cursor.execute(query)
    
    cursor.close()
    conn.close()