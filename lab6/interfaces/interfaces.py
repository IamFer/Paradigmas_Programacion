#==========================================================#
#  El archivo basededatos.py : TRAE EL OBJETO BaseDeDatos  #
#==========================================================#
from aplicacion.repositorio.basededatos import BaseDeDatos

#============================================================#
#  Del directorio aplicacion, el subdirectorio repositorio,  #
#  el archivo s3.py : TRAE EL OBJETO S3                      #
#============================================================#
from aplicacion.repositorio.s3 import S3

#======================================================================#
#  Del directorio aplicacion, el subdirectorio repositorio,            #
#  el archivo sistemadearchivos.py : TRAE EL OBJETO SistemaDeArchivos  #
#======================================================================#
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#======================================================================#
#  Del directorio aplicacion, el subdirectorio modelos, el archivo     #
#  usuario.py : TRAE EL OBJETO Usuario
#======================================================================#
from aplicacion.modelos.usuario import Usuario

#======================================================================#
#  Del directorio aplicacion, el subdirectorio negocios, el archivo    #
#  manejodeinscripciones.py : TREA EL OBJETO ManejoDeInscripciones     #
#======================================================================#
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#====================================#
#       Crear el objeto Usuario      #
#====================================#
usuario = Usuario("Roberto", "Jimenez", 18)

#====================================#
#         Crear el objeto S3         #
#====================================#
repositorioS3 = S3("321321321", "sdf324223", "MiCubeta")

#======================================================================#
#      Interface inscribirUsuario del objeto ManejoDeInscripciones     #
#======================================================================#
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioS3)
print("\n")

#=====================================#
#  Crear el objeto sistemadearchivos  #
#=====================================#
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#======================================================================#
#      Interface inscribirUsuario del objeto ManejoDeInscripciones     #
#======================================================================#
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioSistemaDeArchivos)
print("\n")

#====================================#
#     Crear el objeto basededatos    #
#====================================#
repositorioBaseDeDatos = BaseDeDatos("localhost", "admin", "admin123")

#======================================================================#
#      Interface inscribirUsuario del objeto ManejoDeInscripciones     #
#======================================================================#
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioBaseDeDatos)
print("\n")