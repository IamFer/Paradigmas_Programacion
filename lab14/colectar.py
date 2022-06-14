from multiprocessing.context import assert_spawning
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2

datas = comm.gather(data, root = 0)

if rank == 0:
    for i in range(size):
        assert datas[i] == (i + 1)**2
else:
    assert datas is None

print(datas)