#===========================================#
#       Abrir un Archivo de Texto           #
#===========================================#
print("====================")
print("¡Bienvenido Usuario!")
print("====================")

nombre = input("Ingrese el nombre de su archivo con su extension: ")

try:
    archivo = open(nombre, 'rb')
except OSError:
    print("Error al abrir el archivo: ", nombre)
    exit()
with archivo:
    print(archivo.read())
