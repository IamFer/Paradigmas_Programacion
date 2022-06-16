from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 40
x = range(n)
m = int(math.ceil(float(len(x)) / size))
x_chunk = list(x[rank * m: (rank + 1) * m])
r_chunk = list(map(math.sqrt, x_chunk))

r = comm.allreduce(r_chunk)
rr = comm.allgather(r_chunk)

# - Marca error pero el codigo esta bien (?)
rrr = comm.gather(r_chunk, root = 1)

if rank == 0:
    print(r)
    print(rr)
    print(rrr)

if rank == 1:
    print(rr)
