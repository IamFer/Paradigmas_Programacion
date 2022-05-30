from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# EJ 1: Enteros
if rank == 0:
    data = numpy.arange(10, dtype = 'i') # - Arreglo del 0 - 9
    comm.Send([data, MPI.INT], dest = 1, tag = 77) # - Envío bloqueante

elif rank == 1:
    data = numpy.empty(10, dtype='i')
    comm.Recv([data, MPI.INT], source = 0, tag = 77)
    print(data)

# EJ 2: Flotantes
if rank == 0:
    data = numpy.arange(10, dtype = numpy.float64)
    comm.Send(data, dest = 1, tag = 13)

elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source = 0, tag = 13)
    print(data)
    

