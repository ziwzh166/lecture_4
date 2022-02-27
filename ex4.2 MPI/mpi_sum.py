# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 22:57:03 2022

@author: zhao
"""

from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



if rank != 0:
    data = np.array(rank)
    comm.Send(data, dest=0)
    print("Sending process: ", data)

    
else:
    #if data type not matching result weird
    total_rank = np.zeros(1,dtype =int)
    data = np.zeros(1,dtype = int)
    for i in range(1,size):
        comm.Recv(data, source = i)
        print('Received data is {} in process: {}'.format(data, i))
        total_rank += data
    print("Sum of the process rank is: ", total_rank)