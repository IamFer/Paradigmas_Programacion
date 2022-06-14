from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10

sendarray = numpy.zeros(n, dtype='i') + rank
recvarray = None

if rank == 0:
    recvarray = numpy.empty([size, n], dtype = 'i')

comm.Gather(sendarray, recvarray, root = 0)

if rank == 0:
    for i in range(size):
        assert numpy.allclose(recvarray[i, :], i)

print(recvarray)