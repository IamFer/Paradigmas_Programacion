#=======================================#
# >> mpiexec -n 4 python3 hola_mpi.py   #
# >> mpirun  -n 4 python3 hola_mpi.py   #
#=======================================#
#       PARA CORRER EN 4 PROCESOS       #
#=======================================#
from mpi4py import MPI

#=======================================#
#       Crear un objeto Comunicador     #
#=======================================#
comunicadores = MPI.COMM_WORLD

#=======================================#
#        NUMERO TOTAL DE PROCESOS       #
#=======================================#
n_procesos = comunicadores.Get_size()

#=======================================#
#  NUMERO IDENTIFICADOR DE ESTE PROCESO #
#=======================================#
quien_soy = comunicadores.Get_rank()

print ("¡Saludos desde el proceso ", str(quien_soy), " de ", str(n_procesos),"!")
