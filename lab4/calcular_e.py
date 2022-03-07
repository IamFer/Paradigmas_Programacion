#===================================================#
#   - ALGORITMO 1:                                  #
#---------------------------------------------------#
#   Serie exponencial                               #
#   Factorizacion de x                              #
#   Negativos con funcion inversa                   #
#===================================================#

def calcular_e_negativo(num):
    n = 200
    x = num
    flag = False

    if x < 0:
        flag = True
        x = -x

    s = 1.0

    for i in range(n, 0, -1):
        s *= x / float(i)
        s += 1.0

    if flag == True:
        s = 1/s

    return s

print(calcular_e_negativo(-100.0))
