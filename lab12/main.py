from Curva import Curva
import matplotlib.pyplot as plt

a = [1.0, 0.0, -1.0, 0.0, 0.0, 1.0, 0.0, -1.0]

curva = Curva(a, 2)
n = 300
dx = 1.0/float(n)

for i in range(0, n):
    r = float(i) * dx

    try:
        [x, y] = curva.interpolacion(2, r)
        plt.scatter(x, y, marker = 'o', color = 'black')

        [x, y] =  curva.interpolacion(1, r)
        plt.scatter(x, y, marker = 'o', color='red')
    except Exception as e:
        print(e)
        break

plt.show()
