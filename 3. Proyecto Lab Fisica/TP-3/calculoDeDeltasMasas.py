def calcular_deltas_acpormasa(aceleracion, delta_aceleracion,acPorMasa):
    return ((delta_aceleracion/aceleracion) + (0.003/0.225))*(acPorMasa) 

# -- Aceleración, Delta de Aceleración y la aceleración * masa total.
ac,ac2,ac3,ac4,ac5 = 0.10, 0.13, 0.21, 0.27, 0.41
deltaAc, deltaAc2, deltaAc3, deltaAc4, deltaAc5 = 0.009, 0.013, 0.027, 0.040, 0.075
aM1, aM2, aM3, aM4, aM5 = 0.022, 0.029, 0.047, 0.06, 0.092

delta_aM = calcular_deltas_acpormasa(ac,deltaAc,aM1)
print(f"delta_aM1: {delta_aM}")
delta_aM = calcular_deltas_acpormasa(ac2,deltaAc2,aM2)
print(f"delta_aM2: {delta_aM}")
delta_aM = calcular_deltas_acpormasa(ac3,deltaAc3,aM3)
print(f"delta_aM3: {delta_aM}")
delta_aM = calcular_deltas_acpormasa(ac4,deltaAc4,aM4)
print(f"delta_aM4: {delta_aM}")
delta_aM = calcular_deltas_acpormasa(ac5,deltaAc5,aM5)
print(f"delta_aM5: {delta_aM}")