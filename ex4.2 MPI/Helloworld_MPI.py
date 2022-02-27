# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:44:53 2022

@author: zhao
"""
#hello.py
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()
print('hello world from process {}'.format(rank) )

