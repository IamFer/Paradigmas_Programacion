from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

n = 10

if rank == 0:
    data = numpy.arange(n, dtype='i')
else:
    data = numpy.empty(n, dtype='i')

comm.Bcast([data, MPI.INT], root = 0)

for i in range(n):
    assert data[i] == i

print(data)