import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función
def f(x, y):
    return 4 * x**2 + 9 * y**2 - 10 * x * y + 3

# Punto P
p_x, p_y, p_z = 1, 1, 6

# Crear los datos para la gráfica
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Graficar el plano xy
ax.plot_surface(X, Y, np.zeros_like(Z), color='yellow')

# Vector normal al plano amarillo
normal = [0, 0, 1]

# Generar puntos en el plano perpendicular
xx, yy = np.meshgrid(x, y)
zz = p_z + normal[0] * (xx - p_x) + normal[1] * (yy - p_y)

# Graficar el plano perpendicular
ax.plot_surface(xx, yy, zz, color='red', alpha=0.5)

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()
6