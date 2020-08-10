import numpy as np
def mimatmul(A,B):   
    N = len(A)
    m = (N,N)
    C = np.zeros(m)
    for i in range(len(A)):
        for b in range(len(A)):
            counter = 0
            for j in range(len(A[i])):
                counter += A[i][j]*B.T[b][j]
            C[i][b] = counter            
    return C
