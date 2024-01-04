from abc import ABC, abstractmethod

class Articulo(ABC):
    def __init__(self, precio):
        self.__precio = precio

    @abstractmethod
    def aumentarPorcentaje(self, porcentaje):
        pass

class Limpieza(Articulo):
    __aumento = 20
    
    def __init__(self, precio):
        super().__init__(precio)

    def aumentarPorcentaje(self, porcentaje):
        return self.__precio + (self.__precio * porcentaje / 100)

    def aumentarPrecio(self):
        return self.aumentarPorcentaje(self.__aumento)

class Comestibles(Articulo):
    __aumento = 15
    
    def __init__(self, precio):
        super().__init__(precio)

    def aumentarPorcentaje(self, porcentaje):
        return self.__precio + (self.__precio * porcentaje / 100)

    def aumentarPrecio(self):
        return self.aumentarPorcentaje(self.__aumento)

class Perfumeria(Articulo):
    __aumento = 18
    
    def __init__(self, precio):
        super().__init__(precio)

    def aumentarPorcentaje(self, porcentaje):
        return self.__precio + (self.__precio * porcentaje / 100)

    def aumentarPrecio(self):
        return self.aumentarPorcentaje(self.__aumento)
