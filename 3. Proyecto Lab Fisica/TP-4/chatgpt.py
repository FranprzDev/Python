import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos en los ejes coordenados
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 8])

# Calculamos la pendiente y la ordenada al origen de la mejor recta
m, b = np.polyfit(x, y, 1)

# Creamos un arreglo de valores x para graficar la recta
x_plot = np.linspace(np.min(x), np.max(x), 100)

# Calculamos los valores correspondientes de y para la recta
y_plot = m*x_plot + b

# Graficamos los puntos y la recta
plt.scatter(x, y)
plt.plot(x_plot, y_plot)
plt.show()

# Imprimimos la ecuación de la recta
print("La ecuación de la recta es y = {}x + {}".format(m, b))