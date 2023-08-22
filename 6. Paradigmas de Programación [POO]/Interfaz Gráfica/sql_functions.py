import sqlite3

def conectar_sql():
    conn = sqlite3.connect('personas.db')
    cursor = conn.cursor()

    query = """CREATE TABLE IF NOT EXISTS personas 
    (
     nombre TEXT,
     apellido TEXT,
     edad TEXT
    )
    """

    cursor.execute(query)
    #La conexión hace el commit
    conn.commit()
    
    cursor.close()
    conn.close()
    
def crear_persona(persona_a_guardar):
    try:
        conn = sqlite3.connect('personas.db')
        cursor = conn.cursor()

        query = "INSERT INTO personas (nombre, apellido, edad) VALUES (?, ?, ?)"
        values = (persona_a_guardar.nombre, persona_a_guardar.apellido, persona_a_guardar.edad)

        cursor.execute(query, values)
        conn.commit()

        print("Se creó la persona correctamente")
    except sqlite3.Error as e:
        print("Error al crear la persona:", e)
    finally:
        cursor.close()
        conn.close()


    
    