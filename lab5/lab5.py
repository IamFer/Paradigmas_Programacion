#===============================================#
#        PROGRAMACION ORIENTADA A OBJETOS       #
#===============================================#
# Una clase para un objeto vacio, no esta tan   #
# vacio, necesita la palabra pass = pasar       #
#===============================================#

class ObjetoVacio:
    pass

#===============================================#
#            nada es un ObjetoVacio             #
#===============================================#

nada = ObjetoVacio()
print(type(nada))

#===============================================#
#                 La clase llanta               #
#===============================================#

class Llanta:
    cuenta = 0 # - Variable 'cuenta' es de toda la clase

    #-----------------------------------------------------------------------#
    # Funcion constructora de identidad __init__ es una funcion reservada   #
    # comienza con uno mismo: self, pero puede ser otro nombre 'mi'         #
    # parametros de entrada = default                                       #
    #-----------------------------------------------------------------------#
    def __init__(mi, radio = 50, ancho = 30, presion = 1.5):
        Llanta.cuenta += 1 # - Variable de la estructura compleja Llanta

        # - Variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#-----------------------------------#
#       Objetos (Instanciados)      #
#-----------------------------------#
llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presion = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)

#-----------------------------------#
# Objeto que contiene otros objetos #
#-----------------------------------#

class Coche:
    def __init__(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche= Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) # - Variable global de la clase
print("Presion de la llanta 4: ", llanta4.presion)
print("Radio de la llanta 4", llanta4.radio)
print("Radio de la llanta 3", llanta3.radio)
print("Presion de la llanta 1 de mi coche", micoche.llanta1.presion)

#===============================================#
#                 Encapsulamiento               #
#===============================================#

#-----------------------------------------------------------------------#
# Uso de la funcion de Python 'property' para poner y obtener atributos #
#-----------------------------------------------------------------------#

class Estudiante:
    def __init__(mi):
        mi.__nombre = ''

    def ponerme_nombre(mi, nombre):
        print("Se llamo a ponerme_nombre")
        mi.__nombre = nombre

    def obtener_nombre(mi):
        print("Se llamo a obtener_nombre")
        return mi.__nombre

    nombre = property(obtener_nombre, ponerme_nombre)

#------------------------------------#
# Crear objeto estudiante sin nombre #
#------------------------------------#
estudiante = Estudiante()

#-----------------------------------------------------------------------#
# Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre  #
# (sin tener que llamar explicitamente la función)                      #
#-----------------------------------------------------------------------#
estudiante.nombre = "Diego"

#-------------------------------------------------------------------#
# Obtener el nombre con el metodo obtener_nombre                    #
# __nombre es una variable encapsulada (no visible desde fuera)     #
# (sin tener que llamar explicitamente a la funcion obtener_nombre) #
#-------------------------------------------------------------------#
print(estudiante.nombre)

#............................#
#      ESTO NO FUNCIONA      #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# print(estudiante.__nombre) #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

#===============================================#
#               Herencia de Clases              #
#===============================================#

class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro(mi):
        p = mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4

        print("Perimetro = ", p)
        return p

#---------------------------------------#
# Su hijo rectángulo                    #
# Rectangulo es hijo de Cuadrilatero    #
# Rectangulo (Cuadrilatero)             #
#---------------------------------------#

class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        super().__init__(a, b, a, b) # - Constructor de su madre

#--------------------#
# Su nieto Cuadrado  #
# Hijo de Rectangulo #
#--------------------#
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        area = self.lado1 ** 2
        return area

#-------------------#
# Crear un cuadrado #
#-------------------#
cuadrado1 = Cuadrado(5)

#------------------------------------------------------#
# Llamar al metodo perimetro de su abuelo Cuadrilatero #
#------------------------------------------------------#
perimetro1 = cuadrado1.perimetro()

#----------------------------------#
#  Llamar a su propio metodo area  #
#----------------------------------#
area1 = cuadrado1.area()

print("Perimetro = ", perimetro1)
print("Area = ", area1)

#==========================================================#
# Sobreescribir un metodo de su madre, abuela, tatarabuela #
# Es volver a definir una funcion ya existente             #
#==========================================================#

#===========================================================================#
#                           INICIA SEGUNDA PARTE                            #
#===========================================================================#


#===============================================#
#      La clase A tiene tres numeros reales     #
#===============================================#

class A:
    __a:float = 0.0
    __b:float = 0.0
    __c:float = 0.0

    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

#===============================================#
#      La clase B tiene dos numeros reales      #
#===============================================#

class B:
    __d:float = 0.0
    __e:float = 0.0

    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e

   #-------------------------------------------#
   #  Metodo sumar todo (internos + externos)  #
   #-------------------------------------------#
    def sumar_todo(self, aa:float, bb:float):
        x:float = self.d + self.e + aa + bb
        return x

#===============================================#
#                   Asociacion                  #
#===============================================#

#-------------------------------------#
#     Usando objetos independientes   #
#-------------------------------------#

objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)

print(objetoB.sumar_todo(objetoA.a, objetoA.b))

#------------------------------------------------#
#   El objeto C tiene dos reales y un objeto A   #
#   El objeto A se instancia dentro de C         #
#------------------------------------------------#

class C:
    __d:float = 0.0
    __e:float = 0.0
    __Aa:A = None

    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e
        self.Aa = A(1.0, 2.0, 3.0) # - A se esta instanciando adentro

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#===============================================#
#                  Composicion                  #
#          Contiene otro objeto dentro          #
#===============================================#

objetoC = C(4.0, 5.0)

print(objetoC.sumar_todo())

#---------------------------------------------------#
# Objeto D tiene dos reales y un objeto A definido  #
# por fuera                                         #
#---------------------------------------------------#

class D:
    __d:float = 0.0
    __e:float = 0.0
    __Aa:A = None

    def __init__(self, d:float, e:float, Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#===============================================#
# Agregacion: Construye el objeto agregado por  #
# fuera                                         #
#===============================================#

objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())
