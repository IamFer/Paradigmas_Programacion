#============================#
#        Clase Curva         #
#============================#

class Curva:
    """
    =========================================================
       Curva construye la curva que pasa por
                    los puntos x
    =========================================================
     - Parametros: x coordenadas ordenadas ((x1), (x2), ...)
                   f propiedades (f1(x), f2(x), ...)
                   dim dimensiones
    =========================================================
    """
    #===========#
    # ATRIBUTOS #
    #===========#
    x: float = []
    dim: int = 3

    #=============#
    # CONSTRUCTOR #
    #=============#
    def __init__(s, x: float = [], dim: int  = 3):
        s.x = x
        s.dim = dim
        s.n: int = int(len(s.x)/s.dim)
        s.l = []
        s.lista_de_puntos()
        s.longitud()

    # LISTA DE PUNTOS
    def lista_de_puntos(s) ->  str:
        print(f"Número de puntos = {str(s.n)}")

        # - Formato de Datos
        s.formato = ""

        for j in range(s.dim):
            s.formato += "%15.8e"

        s.formato += "\n"

        # - Tupla de variables a imprimir
        for i in range (0, s.n):
            s.tup = (s.x[i],)

            for ii in range(1, s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)

            print(s.formato % s.tup)

    # LONGITUD PUNTO A PUNTO
    def longitud(s) -> None:
        t: float = 0.0

        for i in range(0, s.n):
            ip1 = i + 1

            if i == s.n - 1:
                ip1 = 0

            d: float = (s.x[ip1] - s.x[i]) ** 2

            for j in range(1, s.dim):
                d += (s.x[ip1 + j * s.n] - s.x[i + j * s.n]) ** 2

            if i == 0: # - Para ptos. equidistantes
                s.dx = d ** 0.5

            t += d ** 0.5
            s.l.append(t)
        s.L = t

    def interpolacion(s, p: int = 0, r: float = 0.0) -> list:
        # - r es el parámetro sobre la curva [0, 1)
        # - p es la suavidad de la curva

        rdx: float = 1.0/s.dx
        xi: float = []
        i: int = int(r * s.L * rdx)
        a: float = r * s.L * rdx - float(i) # - Distancia normalizada

        # INTERPOLACION LINEAL C0
        if p == 0:
            ip1: int = i + 1

            if i == s.n - 1:
                ip1 = 0

            xi.append(a * s.x[ip1] + (1.0 - a) * s.x[i])

            for j in range (1, s.dim):
                xi.append(a * s.x[ipl1 + j * s.n] + (1.0 - a) * s.x[i + j * s.n])

        # INTERPOLACION CUBICA C1
        elif p == 1:
            ip1: int = i + 1
            ip2: int = i + 2

            if i == s.n - 1:
                ip1 = 0
                ip2 = 1
            if i == s.n - 2:
                ip2 = 0
            
            im1: int = i - 1

            if i == 0:
                im1 = s.n - 1

            am1: float = a + 1.0
            ap1: float = 1.0 - a
            ap2: float = 2.0 - a
            z: float = 1.0 - 2.5 * a * a + 1.5 * a * a * a
            zp1: float = 1.0 - 2.5  * ap1 * ap1 + 1.5 * ap1 * ap1 * ap1
            zp2: float = 0.5 * (2.0 - ap2) * (2.0 - ap2) * (1.0 - ap2)
            zm1: float = 0.5 * (2.0 - am1) * (2.0 - am1) * (1.0 - am1)
            xi.append(zp1 * s.x[ip1] + z * s.x[i] + zp2 * s.x[ip2] + zm1 * s.x[im1])

            for j in range(1, s.dim):
                xi.append(zp1 * s.x[ip1 + j * s.n] + z * s.x[i + j * s.n] + zp2 * s.x[ip2 + j * s.n] + zm1 * s.x[im1 + j * s.n])

        # INTERPOLACON QUÍNTICA C2
        elif p == 2:
           ip1: int = i + 1
           ip2: int = i + 2
           ip3: int = i + 3

           if i == s.n - 1:
               ip1 = 0
               ip2 = 1
               ip3 = 2

           if i == s.n - 2:
               ip2 = 0
               ip3 = 1

           if i == s.n - 3:
               ip3 = 0

           im1: int = i - 1
           im2: int = 1 - 2

           if i == 0:
               im1 = s.n - 1
               im2 = s.n - 2
           if i == 1:
               im2 = s.n - 1
           
           u12: float = 1.0 / 12.0
           am1: float = a + 1.0
           am2: float = a + 2.0
           ap1: float = 1.0 - a
           ap2: float = 2.0 - a
           ap3: float = 3.0 - a
           z: float = 1.0 + a * a * u12 * (-15.0 + a * (-35.0 + a * (63.0 + a * (-25.0))))
           zp1: float = 1.0 + ap1 * ap1 * u12 * (-15.0 + ap1 * (-35.0 + ap1 * (63.0 + ap1 * (-25.0))))
           zp2: float = -4.0 + u12 * ap2 * (225.0 + ap2 * (-367.5 + ap2 * (272.5 + ap2 * (-94.5 + 12.5 * ap2))))
           zp3: float = 18.0 + u12 * ap3 * (-459.0 + ap3 * (382.5 + ap3 * (-156.5 + ap3 * (31.5 - 2.5 * ap3))))
           zm1: float = -4.0 + u12 * am1 * (225.0 + am1 * (-367.5 + am1 * (272.5 + am1 * (-94.5 + 12.5 * am1))))
           zm2: float = 18.0 + u12 * am2 * (-459.0 + am2 * (382.5 + am2 * (-156.5 + am2 * (31.5 - 2.5 * am2))))
           xi.append(zp1 * s.x[ip1]+ z * s.x[i] + zp2 * s.x[ip2] + zp3 * s.x[ip3] + zm1 * s.x[im1] + zm2 * s.x[im2])
           for j in range(1, s.dim):
               xi.append(zp1 * s.x[ip1 + j * s.n] + z * s.x[i + j * s.n] + zp2 * s.x[ip2 + j * s.n] + zp3 * s.x[ip3 + j * s.n] + zm1 * s.x[im1 + j * s.n] + zm2 * s.x[im2 + j * s.n])

        else:
            print("La suavidad debe ser 0, 1 o 2")

        return xi
