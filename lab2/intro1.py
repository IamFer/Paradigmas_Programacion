'''
============================================================
                Este es un supercomentario de
                   inicio a nuestro resumen
============================================================
'''

#==========================================================#
#                                                          #
#                   OPERACIONES BASICAS                    #
#                                                          #
#==========================================================#

print(2 + 3)
print(2 * 3)
print(2 / 3)
print(2 ** 10)
print(2 ** 0.5)  # Raíz Cuadrada
print(10 % 2)
print(10 % 0.1)  # - Exclusivamente en Python

#===========================================================#
#                                                           #
#           Para saber el tipo de objeto, se usa            #
#                           type                            #
#                                                           #
#===========================================================#

t = 0
print(type(t)) # ENTERO

t = 3.6
print(type(t)) # REAL (flotante)

t = True
print(type(t)) # BOOLEANO (bool)


#===========================================================#
#                                                           #
#                   Mensajes a Pantalla                     #
#                                                           #
#===========================================================#


print("Este es un comando de Python.", "Este es otro enunciado", t)
print('id: ', 1)
print('First Name: ', 'Steve')
print('Last Name: ', 'Jobs')
print("Vamos a sumar esto" + "con esto otro")


#===========================================================#
#                                                           #
#              Continuar una instruccion en                 #
#                     varios renglones                      #
#                                                           #
#===========================================================#

if 100 > 99 and \
    200 <= 300 and \
    True != False:
        print('Hello World')

#===========================================================#
#                                                           #
#          Comandos diferentes en la misma línea            #
#                                                           #
#===========================================================#

print("¡¡Hola "); print("tu!!")  # - Se considera mala práctica

#===========================================================#
#                                                           #
#      Usando paréntesis redondos, cuadrados o llaves       #
#          se puede escribir en varios renglones            #
#                                                           #
#===========================================================#

list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(list)
print(matriz)

#===========================================================#
#                                                           #
#    Identación estricta para procesos dependientes de      #
#               :  (dos puntos)                             #
#                                                           #
#===========================================================#

if 10 > 5:
    print("Diez es mayor que cinco")
    print("otra identación")

for i in list:
    print(i)
    print("OK")

if 10 > 5:
    print("Verdadero")

    if 10 < 20:
        print("Verdadero")

elif 5 > 3:   # - Comienza segundo condicional
    print("Esto no se imprimira")

else:
    print("Aqui nunca llega")
    
#===========================================================#
#                                                           #
#                        Funciones                          #
#                                                           #
#===========================================================#

def say_hello(name):
    print("Hola ", name)
    print("Welcome to Python Tutorials!")

say_hello("Fernando")

#========================================================================#
#                    INICIA SEGUNDA PARTE DEL APUNTE                     #
#========================================================================#

print("------------- PARTE 2 DEL APUNTE ----------------------")


#===========================================================#
#                                                           #
#    Input permite obtener datos del usuario en prompter    #
#                                                           #
#===========================================================#

nombre = input("Dame tu nombre: ")
print("¡Hola!, ¿Como estas "+ nombre  +"?")


#===========================================================#
#                                                           #
#         Los enteros son de precisión ilimitada            #
#                                                           #
#===========================================================#

y = 5000000000000000000000000000000000
print(y)

#===========================================================#
#                                                           #
#    Se pueden delimitar números con guión bajo pero no     #
#                      con  coma                            #
#===========================================================#

y = 5_000_000
print(y)

#===========================================================#
#                                                           #
#    La función int() cambia strings y floats a enteros     #
#                                                           #
#===========================================================#

numero = int(input("Dame tu edad: "))
type(numero)

#===========================================================#
#                                                           #
#    La notación cientifica de flotantes utiliza e o E      #
#                   1.2 x 10²{-9}                           #
#===========================================================#

y = 1.2E-09
print(y)

#===========================================================#
#                                                           #
#  La funcion float() convierte Strings y enteros a floats  #
#                                                           #
#===========================================================#

y = float("14.3")
print(y)

#===========================================================#
#                                                           #
#  Los complejos se escriben con la raíz de menos uno j     #
#  siempre con un numero como prefijo, no acepta la j       #
#  suelta                                                   #
#                                                           #
#===========================================================#

z = 1 + 1j

#===========================================================#
# Suma +                                                    #
# Resta -                                                   #
# Multiplicación *                                          #
# Division /                                                #
# Módulo %                                                  #
# Exponente **                                              #
# // Funcion piso                                           #
#  Funciones para transformar numeros                       #
#  int(), float(), complex()                                #
#                                                           #
#  Operaciones abs() round() pow()                          #
#===========================================================#

print(round(3.14159,4))


#===========================================================#
#                                                           #
#                String en varias líneas                    #
#                                                           #
#===========================================================#

parrafo = ''' En el bosque de la china 
 la chinita se perdio '''

print(parrafo)

#===========================================================#
#                                                           #
#      La funcion len() obtiene el tamaño del String        #
#                                                           #
#===========================================================#

n = len(parrafo)
print(n)

#===========================================================#
#                                                           #
#   Las letras en un string ocupan lugares como en un       #
#   arreglo (tambien de atras para adelante comenzando en   #
#   -1 el ultimo.                                           #
#                                                           #
#===========================================================#

palabra = "Hola"
print(palabra[0])
print(palabra[-4])

