#Este es sobre Laboratorio de Física 
#En este proyecto, haré todos los cálculos asociados a la matemática que puedo llegar a hacer.

def calcularAceleracion(tiempo):
    aceleracion = 2*1/(tiempo**2)
    return aceleracion

aceleracion1 = calcularAceleracion(4.5)
aceleracion2 = calcularAceleracion(4)
aceleracion3 = calcularAceleracion(3.1)
aceleracion4 = calcularAceleracion(2.7)
aceleracion5 = calcularAceleracion(2.2)
 
#print(f"La aceleracion 1 es: {aceleracion1}")
#print(f"La aceleracion 2 es: {aceleracion2}")
#print(f"La aceleracion 3 es: {aceleracion3}")
#print(f"La aceleracion 4 es: {aceleracion4}")
#print(f"La aceleracion 5 es: {aceleracion5}")
#Los comento ya que luego importo este mod

#No se hace un redondeo, se hace manual porque python redondea de forma
#diferente a como yo lo necesito.