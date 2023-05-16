# Crear una clase Auto, que permita tener los atributos, patente, color, y modelo. 
# Dar de alta dos autos como nuevos objetos.

class Auto: # Definición de la clase 'auto'
    
    # Método Constructor
    def __init__(self, patente, color, modelo):
        # el self es un parecido a .this en Java
        self._patente = patente 
        self._color = color
        self._modelo = modelo
        # La '_' es una conveción general.
        
# Instanciación de los objetos mediante la clase.
auto1 = Auto('XX874XX','Morado', 'VW Voyage')
auto2 = Auto('XX875XX','Verde', 'VW Vento')

# Imprimo los atributos del primer auto: 
print(f'El primer auto tiene las siguientes propiedades: ')
print(f'Patente: {auto1._patente}') 
print(f'Color: {auto1._color}') 
print(f'Modelo: {auto1._modelo}') 

print('')

# Imprimo los atributos del segundo auto: 
print(f'El segundo auto tiene las siguientes propiedades: ')
print(f'Patente: {auto2._patente}') 
print(f'Color: {auto2._color}') 
print(f'Modelo: {auto2._modelo}') 
