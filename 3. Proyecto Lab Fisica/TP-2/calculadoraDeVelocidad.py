import math

tiempo= math.sqrt(2*25/978.9)
deltaT = (1/2*((0.1/25)+(0.1/978.9))*tiempo)
altura = 111.8
velocidadInicial = altura/tiempo
deltaVelocidad = ((3.59/111.8)+(0.0005/0.2260))*494.68

print(f"Tiempo: {tiempo} [s]")
print(f"Delta tiempo: {deltaT} [s]")
print(f"Velocidad inicial (Altura/Tiempo): {velocidadInicial} [cm/s]")
print(f"Delta Velocidad: {deltaVelocidad}")