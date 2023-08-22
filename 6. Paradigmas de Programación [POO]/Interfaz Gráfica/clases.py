class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
    
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad  # Corrección aquí
        
    def __str__(self):
        return f"Nombre: {self.__nombre}\nApellido: {self.__apellido}\nEdad: {self.__edad}"
