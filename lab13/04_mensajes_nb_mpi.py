from mpi4py import MPI

#----------------#
# Objeto mensaje #
#----------------#
class Mensaje:
    def __init__(self, rank):
        self.x = [i for i in range(rank * 10)]
        self.p = "¡Vengo del proceso " + str(rank)  + "!"

# ----- Programa principal ----- #
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank - 1 if rank != 0 else size - 1
    dst = rank + 1 if rank != size - 1 else 0

    comm.isend(s, dest = dst) # - Envio no bloqueante

    # ----- Recibir no bloqueante con espera ----- #
    # ----- req: request (peticion)          ----- #

    req  =comm.irecv(source = src)
    a = req.wait()

    print("Soy el proceso ", rank, " el resultado es ", len(a.x), "", a.p)
