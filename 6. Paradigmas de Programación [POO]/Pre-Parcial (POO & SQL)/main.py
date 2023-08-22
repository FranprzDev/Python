# Francisco Miguel Perez - 2K1 - 56355
import classExamen as c
import os

# Inicialización de Variables Necesarias
corte = 1

fabrica = c.Fabrica()

while corte:
    print('¿Qué tipo de paquete de galletita desea generar (enviar la marca)?')
    
    print('1. Paquete de "Cofler" - 10 galletitas')
    print('2. Paquete de "Saladix" - 25 galletitas')
    print('3. Paquete de "Diversion" - 30 galletitas')
    
    paquete_galletas_marca = input('Ingrese el paquete: ')
    
    if paquete_galletas_marca == "Cofler" or paquete_galletas_marca == "cofler":
        paquete_galleta = c.Paquetes_Galletitas(fabrica, 1)
    elif paquete_galletas_marca == "Saladix" or paquete_galletas_marca == "saladix":
        paquete_galleta = c.Paquetes_Galletitas(fabrica, 2)
    elif paquete_galletas_marca == "Diversion" or paquete_galletas_marca == "diversion":
        paquete_galleta = c.Paquetes_Galletitas(fabrica, 3)
    
    print('¿Desea seguir ingresando paquetes?')
    print('0- No ; 1- Si')
    corte = int(input('Su opcion: '))
    os.system('cls')

os.system('cls')
print(f'Se hicieron un total de {fabrica.get_obtener_galletitas_total()} galletitas')
