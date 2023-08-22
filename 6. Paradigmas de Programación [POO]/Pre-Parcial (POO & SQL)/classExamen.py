class Fabrica():
    def __init__(self):
        self.__cantidad_galletitas_total = 0
        self.__caja = Caja()
    
    def get_obtener_galletitas_total(self):
        return self.__cantidad_galletitas_total
    
    def enviar_paquete(self):
        return self.__caja
    
    def aumentar_galletitas(self, galletitas):
        self.__cantidad_galletitas_total += galletitas
    
    def recibir_paquete(self, tipo_galletita, cantidad_galletitas):
        self.__caja.recibir_paquete(tipo_galletita, cantidad_galletitas)
    

class Caja():
    def __init__(self):
        self.__cantidad_maxima_paquetes = 10
        self.__array_nombre_paquetes = []
        self.__cant_galletitas_total_caja = 0
        self.__caja_llena = False
        
    def comprobar_caja_llena(self):
        if len(self.__array_nombre_paquetes) >= 1 and len(self.__array_nombre_paquetes) <= 9:
            return False
        else:
            return True     
                     
    def recibir_paquete(self, tipo_galletita, cantidad_galletitas):
        if not self.__caja_llena:
            self.__cant_galletitas_total_caja += cantidad_galletitas
            self.__array_nombre_paquetes.append(tipo_galletita)
        else:
            self.__array_nombre_paquetes = []
            self.__caja_llena = False
            self.__array_nombre_paquetes.append(tipo_galletita)
            self.__cant_galletitas_total_caja += cantidad_galletitas


class Paquetes_Galletitas():
    def __init__(self, fabrica, tipo_de_galletas):
        self.__tipo_de_galletas = tipo_de_galletas
        self.__cantidad_galletitas = 0
        if self.__tipo_de_galletas == 1:
            self.__cantidad_galletitas = 10
        elif self.__tipo_de_galletas == 2:
            self.__cantidad_galletitas = 25
        elif self.__tipo_de_galletas == 3:
            self.__cantidad_galletitas = 30
        
        self.__fabrica = fabrica
        self.__fabrica.recibir_paquete(self.__tipo_de_galletas, self.__cantidad_galletitas)
        self.__fabrica.aumentar_galletitas(self.__cantidad_galletitas)
