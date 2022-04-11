#===============================================#
#      Manejo de Archivos usando Python         #
#               Crear Archivo                   #
#===============================================#
print("====================")
print("¡Bienvenido Usuario!")
print("====================")

nombre = input("Ingrese el nombre de su archivo de texto: ")

print("\n==> Creando nuevo archivo de texto...", nombre,".txt")
archivo= open(f"{nombre}.txt", "w")

print("\n¡ARCHIVO CREADO CORRECTAMENTE!")
