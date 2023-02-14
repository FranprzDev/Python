def calcularAceleracion_por_Masa(aceleracion):
    masaTotal = 0.225
    return aceleracion*masaTotal

aceleracion_por_masa_1 = calcularAceleracion_por_Masa(0.10)
print(f"La a*m 1 es: {aceleracion_por_masa_1} Newton")

aceleracion_por_masa_2 = calcularAceleracion_por_Masa(0.13)
print(f"La a*m 2 es: {aceleracion_por_masa_2} Newton")

aceleracion_por_masa_3 = calcularAceleracion_por_Masa(0.21)
print(f"La a*m 3 es: {aceleracion_por_masa_3} Newton")

aceleracion_por_masa_4 = calcularAceleracion_por_Masa(0.27)
print(f"La a*m 4 es: {aceleracion_por_masa_4} Newton")
    
aceleracion_por_masa_5 = calcularAceleracion_por_Masa(0.41)
print(f"La a*m 5 es: {aceleracion_por_masa_5} Newton")

