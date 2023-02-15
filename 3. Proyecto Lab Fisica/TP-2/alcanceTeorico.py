import math

def calcular_alcance_teorico(grados):
    radianes = grados * math.pi / 180
    return (494.68**2)*math.sin(radianes*2)/978.9

def calcular_delta_alcance_teorico(grados, alcanceTeorico):
    radianes = grados * math.pi / 180
    delta_alcance_teorico = ((2*16.98/494.68)+(0.1/978.9)+(2*math.cos(radianes*2)*0.017/math.sin(radianes*2)))*alcanceTeorico
    return delta_alcance_teorico
    
alcanceTeorico30 = calcular_alcance_teorico(30)
delta_alcance_teorico30 = calcular_delta_alcance_teorico(30, alcanceTeorico30)
alcanceTeorico45 = calcular_alcance_teorico(45)
delta_alcance_teorico45 = calcular_delta_alcance_teorico(45, alcanceTeorico45)
alcanceTeorico60 = calcular_alcance_teorico(60)
delta_alcance_teorico60 = calcular_delta_alcance_teorico(60, alcanceTeorico60)

print("Alcances Teoricos (Alcance +/- deltaAlcance): ")
print(f"30 Grados: ( {alcanceTeorico30} +/- {delta_alcance_teorico30} ) [cm]")
print(f"45 Grados: ( {alcanceTeorico45} +/- {delta_alcance_teorico45} ) [cm]")
print(f"60 Grados: ( {alcanceTeorico60} +/- {delta_alcance_teorico60} ) [cm]")

