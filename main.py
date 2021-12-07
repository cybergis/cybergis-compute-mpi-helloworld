# MPI-enabled

import os
import pprint as pp
from distutils.dir_util import copy_tree
from mpi4py import MPI

# init mpi env
comm = MPI.COMM_WORLD
# id/rank in mpi env
rank = comm.Get_rank()
# size of the mpi cluster
size = comm.Get_size()
# processor name
hostname = MPI.Get_processor_name()

# all processes to print Hello World
print("Hello World ! main.py {}/{}@{}".format(rank, size, hostname))

# rank 0 to do something
if rank == 0:
   # print some environment variables
   my_environ_keys = ["data_folder", "executable_folder", "hpc", "job_id", "result_folder", "user_id", "SLURM_JOB_ID"]
   environ_subset = {key: os.environ.get(key, "NULL") for key in my_environ_keys}
   pp.pprint(environ_subset, width=1)
   
   #copy input file(s) to result_folder 
   copy_tree(environ_subset["data_folder"], environ_subset["result_folder"])
   
comm.Barrier()

# all processes to print Done
print("Done! main.py {}/{}@{}".format(rank, size, hostname))
