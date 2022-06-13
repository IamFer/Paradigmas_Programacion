import numpy as np
import matplotlib.pyplot as plt
import time

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# - Numero de celdas
n = np.array([512, 512])
# - Tamaño del dominio
L = np.array([1.0, 1.0])
# - Constante de difusión
k = 0.2
# - Pasos de tiempo
pasos = 100

dx = L/n
udx2 = 1.0/(dx*dx)

dt = 0.25 * (min(dx[0], dx[1])**2)/k
print("dt = ", dt)

nt = n[0] * n[1]
print("Celdas = ", nt)

u = np.zeros(nt, dtype = np.float64)
un = np.zeros(nt, dtype = np.float64)

def evolucion(u, n, udx2, dt, i, k):
    jp1 = i + n[0]
    jm1 = i - n[0]
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1]) * udx2[0] + (u[jm1] - 2.0*u[i] + u[jp1])  * udx2[1]
    unueva = u[i] + dt * k * laplaciano
    return unueva

def solucion(u, un, udx2, dt, n , k):
    for jj in range(1, n[1] - 1):
        for ii in range(1, n[0] - 1):
            i = ii + n[0] * jj
            unueva = evolucion(u, n, udx2, dt, i , k)

            if i == int(nt/2) + int(n[0]/2):
                unueva = 1.0

            un[i] = unueva

start = time.time()

for t in range(1, pasos + 1):
    solucion(u, un, udx2, dt, n, k)
    u = un

    if t % 100 == 0:
        print("Iteración = ", t)

end = time.time()
print("Tardó", end-start, "s")

u = np.reshape(u, (n[0], n[1]))
x, y = np.meshgrid(np.arange(0, L[0], dx[0]), np.arange(0, L[1], dx[1]))
ax = plt.axes(projection = '3d')
ax.plot_surface(x, y, u, cmap = cm.hsv)
plt.show()
