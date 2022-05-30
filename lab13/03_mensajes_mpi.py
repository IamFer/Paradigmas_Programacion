from mpi4py import MPI

#----------------#
# Objeto mensaje #
#----------------#
class Mensaje:
    def __init__(self, rank):
        self.x = range(rank * 10) # Iterador
        self.p = "¡Vengo del proceso " + str(rank)  + "!"

# ----- Programa principal ----- #
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    #print(s.x)

    # ----- Que te mande el anterior y si es cero que sea el último ----- #
    fuente = rank - 1 if rank != 0 else size - 1

    # ----- Mándalo al siguiente y si eres el último mandalo al primero ----- #
    destino = rank + 1 if rank != size - 1 else 0

    #===========================================================#
    # send y recv son operaciones bloqueadas y generan que el   #
    # codigo se atore esperando que alguien reciba un mensaje   #
    # esto se resuelve enviando con los pares y recibiendo con  #
    # los impares                                               #
    #===========================================================#
    
    if rank % 2 == 0: # - Si es PAR
        comm.send(s, dest = destino) # - Enviar mensaje s al dest
        m = comm.recv(source = fuente) # - Recibir de spurce y lo pone en m

    else: # - Si es IMPAR
        # ----- Recibir primero y mandar mensaje despues  ----- #
        m = comm.recv(source = fuente)
        comm.send(s, dest = destino)

    print("Soy el proceso ", rank, " el resultado es ", len(m.x), "", m.p)

