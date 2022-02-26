
zhao@DESKTOP-8PHCC8L:/mnt/c/Users/zzw/OneDrive/python/lecture_4/ex4.1 cython$ kernprof -l -v rbf.py
Python:  38.04173827171326
Scipy:  0.18801188468933105
Cython:  0.1554098129272461
Wrote profile results to rbf.py.lprof
Timer unit: 1e-06 s

Total time: 21.8896 s
File: rbf.py
Function: rbf_network at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           # Naive python implementation of a Radial Basis Function (RBF) approximation scheme
     6                                           def rbf_network(X, beta, theta):
     7
     8         1          8.0      8.0      0.0      N = X.shape[0]
     9         1          2.0      2.0      0.0      D = X.shape[1]
    10         1          6.0      6.0      0.0      Y = np.zeros(N)
    11
    12      1001       1125.0      1.1      0.0      for i in range(N):
    13   1001000    1105456.0      1.1      5.1          for j in range(N):
    14   1000000    1082768.0      1.1      4.9              r = 0
    15   6000000    6718961.0      1.1     30.7              for d in range(D):
    16   5000000    9410462.0      1.9     43.0                  r += (X[j, d] - X[i, d]) ** 2
    17   1000000    1256666.0      1.3      5.7              r = r**0.5
    18   1000000    2314145.0      2.3     10.6              Y[i] += beta[j] * exp(-(r * theta)**2)
    19
    20         1          1.0      1.0      0.0      return Y

Total time: 0.187958 s
File: rbf.py
Function: rbf_scipy at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           # Scipy implementation of a Radial Basis Function (RBF) approximation scheme
    23                                           def rbf_scipy(X, beta):
    24
    25         1          5.0      5.0      0.0      N = X.shape[0]
    26         1          1.0      1.0      0.0      D = X.shape[1]
    27         1     135981.0 135981.0     72.3      rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    28                                               #Xtuple = tuple([X[:, i] for i in range(D)])
    29         1         29.0     29.0      0.0      Xtuple = tuple([X[:, i] for i in range(D)])
    30
    31         1      51942.0  51942.0     27.6      return rbf(*Xtuple)

