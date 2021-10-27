from mpi4py import MPI
import os
import pprint

# init mpi
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = MPI.Get_processor_name()


print("Hello World ! main.py {}/{}@{}".format(rank, size, hostname))

if rank == 0:
   pprint(os.environ)
comm.Barrier()


print("Done! main.py {}/{}@{}".format(rank, size, hostname))
