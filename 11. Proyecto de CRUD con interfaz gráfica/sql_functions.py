import sqlite3
import os

# Operación para crear la tabla 'profesores'
def conectar_sql():
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)
    
    conn = sqlite3.connect('professor.db')
    cursor = conn.cursor()

    query = """CREATE TABLE IF NOT EXISTS profesores 
    (legajo INTEGER PRIMARY KEY, 
     nombre TEXT,
     apellido TEXT,
     edad INTEGER,
     materia TEXT,
     antiguedadAnios INTEGER,
     comisiones TEXT
    )
    """

    cursor.execute(query)
    #La conexión hace el commit
    conn.commit()
    
    cursor.close()
    conn.close()

# Operacion de Buscar un profe como objeto o si este existe
def buscar_profe_obj(legajo):
    conn = sqlite3.connect('professor.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM profesores WHERE legajo=?",(legajo,))
    profe_obj = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return profe_obj

def buscar_profesor(legajo):
    conn = sqlite3.connect('professor.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM profesores WHERE id=?", (legajo,))
    profesor_encontrado = cursor.fetchone()
    
    cursor.close()
    conn.close()
    if(profesor_encontrado):
        return True
    else:
        return False

# Operacion de Crear un profesor en la tabla
def crear_profesor(profesor):
    #if(buscar_profesor(profesor.get_legajo())):
        conn = sqlite3.connect('professor.db')
        cursor = conn.cursor()
        
        profe = (profesor.get_legajo(), profesor.get_nombre(), profesor.get_apellido(), 
             profesor.get_edad(), profesor.get_materia(), 
             profesor.get_antiguedadAnios(), profesor.get_comisiones())
    
        cursor.execute('INSERT INTO profesores (id, nombre, apellido, edad, materia, antiguedadAnios, comisiones) VALUES (?, ?, ?, ?, ?, ?, ?)', profe)

    
        conn.commit()
        cursor.close()
        conn.close()
    #else:
     #   print('Legajo ya encontrado...')

# Operación para remover un profesor
def remover_profesor_legajo(legajo):
    if(buscar_profesor(legajo)):
        conn = sqlite3.connect('professor.db')
        cursor  = conn.cursor()

        cursor.execute('DELETE FROM profesor WHERE legajo=?', (legajo,))
        print(f'Se elimino el profesor con el legajo {legajo}')
        
        conn.commit()
        
        cursor.close()
        conn.close()

def actualizar_edad(legajo, edad):
    profe = buscar_profesor(legajo)
    if(profe):
      conn = sqlite3.connect('professor.db')
      cursor = conn.cursor()
      
      cursor.execute('UPDATE profesor SET edad=? WHERE legajo=?', (edad, legajo))
      
      print(f'Se actualizó correctamente el profesor con su nueva edad')
      conn.commit()
      cursor.close()
      conn.close()  
    else:
        print('No se pudo encontrar el profesor.')
    
def actualizar_antiguedad(legajo):
    # la antiguedad se da en anios
    profe = buscar_profe_obj(legajo)
    antiguedad = int(profe.get_antiguedad())
    antiguedad += 1
    
    if(profe):
        conn = sqlite3.connect('professor.db')
        cursor = conn.cursor()
        
        cursor.execute('UPDATE profesor SET antiguedad=? WHERE legajo=?', (antiguedad,legajo))
        
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print('No se pudo encontrar el profesor.')

def aniadir_comision(legajo, comision):
    pass