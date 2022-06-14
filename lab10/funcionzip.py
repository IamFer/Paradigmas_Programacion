mi_lista = [1, 2, 3]
tu_lista = (10, 20, 30)
su_lista = (40, 50, 100)

def multiplicar_por2(elemento):
    return elemento * 2

def solo_impar(elemento):
    return elemento % 2 != 0

print(list(zip(mi_lista, tu_lista, su_lista)))

una_lista = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)

cuadrados = (x*x for x in range(5))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

import math
print(sum(x*x for x in range(5)))

numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range(21) if x % 2 == 0])
print(numeros_pares)