#Para hacer esta calculadora debemos realizar un promedio..
def calcularPromedio(x1,x2,x3,x4,x5):
    return (x1+x2+x3+x4+x5)/5

x1,x2,x3,x4,x5 = 109.0,115.0,112.0,108.0,115.0
promedio = calcularPromedio(x1,x2,x3,x4,x5)
print(f"Xprom = {promedio} [cm]")