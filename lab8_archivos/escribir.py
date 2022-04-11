#===============================#
#     Escribir dentro de un     # 
#            archivo            #
#===============================#

print("====================")
print("¡Bienvenido Usuario!")
print("====================\n")

nombre = input("Ingrese el nombre de su archivo con extension en donde va a escribir: ")

try:
    archivo = open(nombre, 'r+')
except OSError:
    print("Error al abrir el archivo: ", nombre)
    exit()
with archivo:
    texto = input("Ingrese lo que va a escribir dentro de el archivo: \n")
    archivo.write(texto)
    archivo.close
    print("\n==> Archivo Escrito Satisfactoriamente.")

