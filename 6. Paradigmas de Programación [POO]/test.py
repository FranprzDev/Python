import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función
def f(x, y):
    condition = np.logical_and(x != 0, y != 0)
    result = np.where(condition, (x * y**2) / (x**3 + y**3), 0)
    return result

# Generar los puntos en el espacio tridimensional
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico de f(x, y)')

# Marcar el punto (0,0)
ax.scatter([0], [0], [0], color='red', s=50, label='Punto (0,0)')

# Calcular y mostrar las derivadas parciales
dZ_dx = (Y**2 * (2 * x**3 - 3 * y**3)) / (x**3 + y**3)**2
dZ_dy = (2 * x * y * (x**3 - y**3)) / (x**3 + y**3)**2

ax.quiver(0, 0, 0, 0.2, 0.2, dZ_dx[0], color='blue', label='Derivada parcial respecto a X')
ax.quiver(0, 0, 0, -0.2, -0.2, dZ_dy.flatten()[0], color='green', label='Derivada parcial respecto a Y')

# Ajustar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()
