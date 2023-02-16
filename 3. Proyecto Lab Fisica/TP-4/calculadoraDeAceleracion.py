def calcularAceleracion(tiempo):
    return (2*0.8)/tiempo**2

def deltaAceleracion(aceleracion, tiempo):
    return ((0.02/0.08)+(2*0.2/tiempo))*aceleracion

ac1 = calcularAceleracion(24.95)
ac2 = calcularAceleracion(12.43)
ac3 = calcularAceleracion(9.99)
ac4 = calcularAceleracion(8.26)
ac5 = calcularAceleracion(6.51)

deltaAceleracion_1 = deltaAceleracion(ac1, 24.95)
deltaAceleracion_2 = deltaAceleracion(ac2, 12.43)
deltaAceleracion_3 = deltaAceleracion(ac3, 9.99)
deltaAceleracion_4 = deltaAceleracion(ac4, 8.26)
deltaAceleracion_5 = deltaAceleracion(ac5, 6.51)

print(f"ac1: {ac1} +/- {deltaAceleracion_1}")
print(f"ac2: {ac2} +/- {deltaAceleracion_2}")
print(f"ac3: {ac3} +/- {deltaAceleracion_3}")
print(f"ac4: {ac4} +/- {deltaAceleracion_4}")
print(f"ac5: {ac5} +/- {deltaAceleracion_5}")
