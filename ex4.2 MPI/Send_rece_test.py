# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 08:35:02 2022

@author: zzw
"""
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    data = np.random.rand(1)
    for i in range(1, size):
        comm.Send(data, dest=i, tag=i)
        print('Process {} sent data:'.format(rank), data)

else:
    # note: the size of the receiving buffer is larger than
    # that of the sending buffer
    data = np.zeros(1)
    comm.Recv(data, source=0, tag=rank)
    print('Process {} has data:'.format(rank), data)