#Calculo el delta de aceleracion
#import ErrorAceleracion as err
# se puede importar si es necesario, si proximamente los valores no cambiaran,
# nuestro estudio es estático, por lo tanto siempre son iguales.

def calcularDeltaAceleracion(tiempo, aceleracion):
    deltaAceleracion = (((0.001)/1)+(2*(0.2/tiempo)))*aceleracion
    return deltaAceleracion

delta_aceleracion_1 = calcularDeltaAceleracion(4.5, 0.10)
delta_aceleracion_2 = calcularDeltaAceleracion(4.0, 0.13)
delta_aceleracion_3 = calcularDeltaAceleracion(3.1, 0.21)
delta_aceleracion_4 = calcularDeltaAceleracion(2.7, 0.27)
delta_aceleracion_5 = calcularDeltaAceleracion(2.2, 0.41)
 
print(f"El delta de aceleracion 1 es: {delta_aceleracion_1}")
print(f"El delta de aceleracion 2 es: {delta_aceleracion_2}")
print(f"El delta de aceleracion 3 es: {delta_aceleracion_3}")
print(f"El delta de aceleracion 4 es: {delta_aceleracion_4}")
print(f"El delta de aceleracion 5 es: {delta_aceleracion_5}")

#No se hace un redondeo, se hace manual porque python redondea de forma
#diferente a como yo lo necesito.