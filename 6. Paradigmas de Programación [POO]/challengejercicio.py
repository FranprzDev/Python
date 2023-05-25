# DISEÑAR TRES CLASES QUE PERMITAN TRABAJAR CON PERSONAS, EMPLEADOS, PASANTES, 
# TOMANDO EL CONCEPTO DE HERENCIA Y ASEGURANDO EL ACCESO A 
# LOS ATRIBUTOS A CADA CLASE. 
# DAR DE ALTA DOS EMPLEADOS Y DOS PANSATES. PROPONER PARA 
# CADA CLASE LO ATRIBUTOS QUE CONSIDERE IMPORTANTES.
# ADEMAS EL EJERCICIO DEBE CONTAR CON GETERS Y SETERS, 
# COMO ASI TAMBIEN CON LOS CONTRUCTORES PARA CADA CLASE.

from numbers import Number
import math


class Persona:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._nacionalidad = nacionalidad
        
    @property #Decorador -> Del tipo 'getter'
    def nombre(self) -> str:
        return self._nombre
        
    @nombre.setter #Decorador -> Del tipo 'setter'
    def nombre(self, nuevo_nombre) -> None:
        self._nombre = nuevo_nombre
           
    @property 
    def apellido(self) -> str:
        return self._apellido
        
    # No tiene mucho sentido de que se pueda cambiar el nombre...
    # Por eso lo dejo comnetado.
    # @apellido.setter
    # def apellido(self, nuevo_apellido):
    #     self.apellido = nuevo_apellido
        
    @property 
    def edad(self) -> str:
        return self._edad
      
    @edad.setter
    def apellido(self, nueva_edad) -> None:
        self._edad = nueva_edad
        
    @property 
    def nacionalidad(self) -> str:
        return self._nacionalidad
    
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad) -> None:
        self._nacionalidad = nueva_nacionalidad

class Empleado(Persona):
    
    def __init__(self, nombre, apellido, edad, nacionalidad, 
                 id_definitivo, puesto, salario, antiguedad, hs_diarias):
        
        # Llamada a la clase padre
        super().__init__(nombre, apellido, edad, nacionalidad)
        
        # Propiedades propias de la Clase "Empleado"
        int(id_definitivo)
        self._id_definitivo = id_definitivo
        self._puesto = puesto
        float(antiguedad)
        self._salario = salario
        int(antiguedad)
        self._antiguedad = antiguedad
        int(hs_diarias)
        self._hs_diarias = hs_diarias
     
    # Método Set & Get -> ID_DEFINITIVO
       
    @property 
    def id_definitivo(self) -> int:
        return self._id_definitivo
    
    # El ID no se cambia, como mucho se borra. (Pero es ajeno a este proceso).
    # @id_definitivo.setter
    # def id_definitivo(self, nuevo_id) -> None:
    #     self._id_definitivo = nuevo_id
    
    # Método Set & Get -> Puesto
    @property 
    def puesto(self) -> str:
        return self._puesto
    
    @puesto.setter
    def puesto(self, nuevo_puesto) -> None:
        self._puesto = nuevo_puesto
        
    # Método Set & Get -> Puesto
    @property 
    def salario(self) -> float:
        return float(self._nuevo_salario)
    
    @salario.setter
    def salario(self, nuevo_salario) -> None:
        self._salario = nuevo_salario
        
    # Método Set & Get -> Antiguedad
    @property 
    def antiguedad(self) -> str:
        return self._antiguedad
    
    @antiguedad.setter
    def antiguedad(self, nueva_antiguedad) -> None:
        self._antiguedad = nueva_antiguedad
        
    # Método Set & Get -> Hs Diarias
    @property 
    def hs_diarias(self, hs_diarias) -> int:
        return self._hs_diarias
    
    @antiguedad.setter
    def hs_diarias(self, nueva_cantidad_hs) -> None:
        self._hs_diarias = nueva_cantidad_hs
        
class  Pasante(Empleado):
    def __init__(self, nombre, apellido, edad, nacionalidad, salario):
        # Iniciación de las variables para la clase super.
        id_definitivo_hard_code = -1
        puesto_hard_code = "Pasante"
        antiguedad_hard_code = 0
        hs_diarias_hard_code = 8
      
        # Envio las clases hardcodeadas.
        super().__init__(nombre, apellido, 
                         edad, nacionalidad, 
                         id_definitivo_hard_code, 
                         puesto_hard_code, salario, 
                         antiguedad_hard_code, 
                         hs_diarias_hard_code)
        
    def datosPasante(self):
        print(f"Nombre: {self._nombre}")
        print(f"Apellido: {self._apellido}")
        print(f"ID Pasante [-1]: {self._id_definitivo}")
        print(f"Horas trabajadas: {self._hs_diarias}")
        
empleado_1 = Empleado("Juan Jose", "Martinez", 23, "Argentino"
                        , "23", "Scrum Master & Rust Developer", 
                        "3500", "2", "6")

empleado_2 = Empleado("Josehmir", "Fasent", 28, "Boliviano"
                        , "24", "Assembler Developer", 
                        "6800", "4", "4")

pasante_1 = Pasante("Mauro", "Lombardo", 26, 
                    "Argentino", "400")

pasante_2 = Pasante("Victoria", "Cardona", 24, 
                    "Puerto Rico", "400")

# Acceder a los atributos y métodos
print(empleado_1._nombre)  # Salida: Juan Jose
print(empleado_1._puesto)  # Salida: Scrum Master & Rust Developer
print(empleado_1._salario)  # Salida: 3500.0
print(empleado_1._antiguedad)  # Salida: 2
empleado_1.antiguedad = 3
print(empleado_1._antiguedad)

print(pasante_1._nombre)  # Salida: Mauro
print(pasante_1._apellido)  # Salida: Lombardo
print(pasante_1._id_definitivo)  # Salida: -1
print(pasante_1._hs_diarias)  # Salida: 8

# Llamar al método datosPasante()
pasante_1.datosPasante()