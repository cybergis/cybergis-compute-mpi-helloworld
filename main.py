from mpi4py import MPI
import os
import pprint as pp

# init mpi
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = MPI.Get_processor_name()


print("Hello World ! main.py {}/{}@{}".format(rank, size, hostname))

if rank == 0:
   my_environ_keys = ["data_folder", "executable_folder", "hpc", "job_id", "result_folder", "user_id", "SLURM_JOB_ID"]
   environ_subset = {key: os.environ.get(key, "NULL") for key in my_environ_keys}
   pp.pprint(environ_subset, width=1)
comm.Barrier()


print("Done! main.py {}/{}@{}".format(rank, size, hostname))
