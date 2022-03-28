from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

class ManejoDeInscripciones: # -¡NO TIENE VARIABLES!
    #=============================================================#
    #  Decorador staticmethod. El objeto solo tiene la funcion    #
    #  inscribirUsuario. ENVUELVE LA FUNCION SIN LLAMAR VARIABLES #
    #  LOCALES. El objeto ManejoDeInscripciones es la interface   #
    #  intercambiable                                             #
    #============================================================#

    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("-------> Guardando Usuario ...")

        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()