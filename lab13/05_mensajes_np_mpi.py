from mpi4py import MPI
import numpy as np

#----------------#
# Objeto mensaje #
#----------------#
class Mensaje:
    def __init__(self, rank):
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "¡Vengo del proceso " + str(rank)  + "!"

# ----- Programa principal ----- #
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank - 1 if rank != 0 else size - 1
    dst = rank + 1 if rank != size - 1 else 0

    m = s.x # - Arreglo para enviar
    #print(m)

    # ----- Isend Irecv son para comunicación ----- #
    # ----- no bloqueante de arreglos de numpy ----- #
    comm.Isend(m, dest = dst)

    #=============================================#
    # Arreglo vacío para recibir con dimension 10 #
    # y tipos de datos float64 (doble precision)  #
    #=============================================#
    a = np.zeros(10, dtype = np.float64)
    req = comm.Irecv(a, source = src)
    req.Wait()

    print("Soy el proceso ", rank, " el resultado es ", a)
