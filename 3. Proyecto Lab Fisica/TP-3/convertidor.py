def masaPunt(masa):
  factor_conversion = 1.5 / 0.001
  posicion = masa * factor_conversion 
  return posicion

def faPunt(fuerza):
  factor_conversion = 4 / 0.03
  posicion = fuerza * factor_conversion
  return posicion

def redPers(numero):
    diferencia = numero - int(numero)
    if diferencia < 0.5:
        return int(numero)
    else:
        return int(numero) + 1

def redondec(numero):
    centesimas = int((numero * 100) % 100)
    if centesimas < 50:
        return round(numero, 2)
    else:
        return round(numero + 0.01, 2)

masa1_X,masa2_X, = masaPunt(0.003),masaPunt(0.004)
masa3_X,masa4_X = masaPunt(0.006),masaPunt(0.007)
masa5_X,errorGral = masaPunt(0.011),masaPunt(0.0001)

newton1_Y,newton2_Y = redPers(faPunt(0.022)), redPers(faPunt(0.029)) 
newton3_Y,newton4_Y = redPers(faPunt(0.047)), redPers(faPunt(0.061))
newton5_Y = redPers(faPunt(0.092))

errorNew1,errorNew2 = redondec(faPunt(0.0023)), redondec(faPunt(0.0033))
errorNew3, errorNew4 = redondec(faPunt(0.0067)),redondec(faPunt(0.0097))
errorNew5 = redondec(faPunt(0.0180))

print(f"Primer Punto (x,y): ({masa1_X} +/- {errorGral},{newton1_Y} +/- {errorNew1})cm")
print(f"Segundo Punto (x,y): ({masa2_X} +/- {errorGral},{newton2_Y} +/- {errorNew2})cm")
print(f"Tercer Punto (x,y): ({masa3_X} +/- {errorGral},{newton3_Y} +/- {errorNew3})cm")
print(f"Cuarto Punto (x,y): ({masa4_X} +/- {errorGral},{newton4_Y} +/- {errorNew4})cm")
print(f"Quinto Punto (x,y): ({masa5_X} +/- {errorGral},{newton5_Y} +/- {errorNew5})cm")