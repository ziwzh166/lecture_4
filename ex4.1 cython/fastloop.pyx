# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:09:55 2022

@author: zhao
"""
from math import exp
import numpy as np

@profile
def rbf_network_cython(double [:,:] X , double [:] beta,int theta):
    cdef int N, D
    N = X.shape[0]
    D = X.shape[1]
    cdef double [:] Y = np.zeros(N)
    cdef int i,j,d
    cdef double r
    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)
    return Y
    



    
    
    
    