def convertir_puntos_a_masa(puntos):
    return puntos * 0.001 / 1.5

def convertir_a_newton(fuerza_y):
    return fuerza_y * 0.03 / 4

punto1_x = 4.5
punto2_x = 9

punto1_y = 3
punto2_y = 6

valorKg_1 = convertir_puntos_a_masa(punto1_x) 
valorKg_2 = convertir_puntos_a_masa(punto2_x)

valorN_1 = convertir_a_newton(punto1_y)
valorN_2 = convertir_a_newton(punto2_y)

print(f"Punto 1: ({valorKg_1}kg,{valorN_1}N)")
print(f"Punto 2: ({valorKg_2}kg,{valorN_2}N)")
