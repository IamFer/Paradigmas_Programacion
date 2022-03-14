#===================================================#
#   - ALGORITMO 1:                                  #
#---------------------------------------------------#
#   Serie exponencial                               #
#   Factorizacion de x                              #
#   Negativos con funcion inversa                   #
#===================================================#

def e(num):
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

print(e(e(e(-1))))
