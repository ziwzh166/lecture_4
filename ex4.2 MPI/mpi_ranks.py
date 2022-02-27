# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 22:38:02 2022

@author: zhao
"""
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()

print('the rank of the process is: ', rank)


#test command "mpirun -n 4 python3 mpi.rank.py" 