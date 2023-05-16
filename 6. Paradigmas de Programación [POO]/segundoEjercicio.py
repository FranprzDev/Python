#2 - (Bajo el punto anterior) A la Clase Auto, encapsular sus atributos y 
# crear los SET y GET para cada uno de ellos.

class Auto:
    def __init__(self, patente, color, modelo):
        self._patente = patente 
        self._color = color
        self._modelo = modelo
        
    # En py, se utilizan los "decoradores" para hacer los métodos GET & SET
    # Para los getters usamos @property & para los setters usamos @propiedad.setter
    
    @property 
    def patente(self):
        return self.patente
    
    @patente.setter
    def patente(self, nueva_patente):
        self._patente = nueva_patente

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo
    
auto1 = Auto('XX874XX','Morado', 'VW Voyage')
auto2 = Auto('XX875XX','Verde', 'VW Vento')

print(f'''PRIMER AUTO:
    Patente: {auto1._patente} 
    Color: {auto1._color} 
    Modelo: {auto1._modelo}''')

print('')

print(f'''SEGUNDO AUTO:
    Patente: {auto2._patente} 
    Color: {auto2._color} 
    Modelo: {auto2._modelo}''')

# Le hago cambios a auto1 y lo imprimo de vuelta
auto1._color = 'Violeta'
auto1._patente = 'AB772QR'

print('')

print(f'''PRIMER AUTO [MODIFICADO]:
    Patente: {auto1._patente} 
    Color: {auto1._color} 
    Modelo: {auto1._modelo}''')