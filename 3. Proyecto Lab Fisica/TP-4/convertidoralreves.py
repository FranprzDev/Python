# Definimos las escalas para cada eje
escala_x = 100  # 1cm cada 0.01 kg
escala_y = 333.33  # 1cm cada 0.003m/s^2

# Definimos los puntos fijos
punto1 = (11, 5.9)
punto2 = (14, 11)

# Convertimos los puntos a la escala de cada eje
x1_cartesiano = punto1[0] / escala_x
y1_cartesiano = punto1[1] / escala_y
x2_cartesiano = punto2[0] / escala_x
y2_cartesiano = punto2[1] / escala_y

# Imprimimos los puntos en el eje cartesiano, convirtiendo las unidades de medida
print("Los puntos en el eje cartesiano son:")
print("- Punto 1: ({:.2f} kg, {:.2f} m/s^2)".format(x1_cartesiano, y1_cartesiano))
print("- Punto 2: ({:.2f} kg, {:.2f} m/s^2)".format(x2_cartesiano, y2_cartesiano))