#=======================================#
#   mpirun -n 4 python3 tareas_mpi.py   #
#=======================================#
from mpi4py import MPI

#===============#
# COMUNICADORES #
#===============#
comm = MPI.COMM_WORLD

#======================#
# CUÁNTOS SON EN TOTAL #
#======================#
size = comm.Get_size()

#==========#
# Quién es #
#==========#
rank = comm.Get_rank()

print("------------------------------------")

#=========================#
# SI SOY EL CERO HACER... #
#=========================#
if rank == 0:
    print("Soy el proceso 0")

#======================================#
# EN OTRO CASO, SI SOY EL UNO HACER... #
#======================================#
elif rank == 1:
    print("Yo soy el proceso 1")

#============================#
# EN CASO CONTRARIO HACER... #
#============================#
else:
    print("Yo no soy ninguno de los dos primeros procesos")

print("Reportando desde el proceso ", str(rank), " de ", str(size))
print("------------------------------------")
