class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__fullname = nombre + ' ' + apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_fullname(self):
        return self.__fullname

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, legajo, materia, antiguedadAnios, comisiones):
        super().__init__(nombre, apellido, edad)
        self.__legajo = legajo
        self.__materia = materia
        self.__antiguedadAnios = antiguedadAnios
        self.__comisiones = comisiones
        
    def aumentar_anios_antiguedad(self):
        self.__antiguedadAnios += 1
        
    def get_materia(self):
        return self.__materia
    
    def get_antiguedadAnios(self):
        return self.__antiguedadAnios
    
    def get_comisiones(self):
        return self.__comisiones
    
    def get_legajo(self):
        return self.__legajo