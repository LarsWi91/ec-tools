r"""
Implementation of an algorithm for 
semi-integration (v=-0.5) and semi-differentiation (v=0.5)
Gruenwald (G1) 
based on
Oldham: Electrochemical Science and Technology, 2012
"""

import numpy as np
from transonic import jit, boost, set_compile_at_import

# set_compile_at_import(True)
# @boost

@jit(backend = 'numba')
def semi_integration(I: "float[:]",t: "float[:]", v:float =-0.5):
    
#def semi_integration(I:A,t:A, v:float=-0.5):
    '''
    TEST:
    >>> import pandas as pd
    >>> from scipy.integrate import cumulative_trapezoid
    >>> df1 = pd.read_csv('../../test/data/Testfile_1.csv')
    >>> np.allclose(semi_integration(semi_integration(df1['I'],df1['t']), df1['t'])[:-1], cumulative_trapezoid(df1['I'],df1['t']), rtol=1e-12)
    True
    >>> df2 = pd.read_csv('../../test/data/Testfile_2.csv')
    >>> np.allclose(semi_integration(semi_integration(df2['I'],df2['t']), df2['t'])[:-1], cumulative_trapezoid(df2['I'],df2['t']), rtol=1e-2)
    True
    '''
    # (equidistant) time step
    delta = t[1]-t[0]
    # No. of steps
    N_max = I.size
    # initialize with zeros
    G1 = np.zeros(N_max)
    for N in range(1,N_max+1):
        # value for n = N with w0 = 1
        G1_i = I[0]; 
        #      go from N to 0
        for n in range(N-1,0,-1):
            G1_i = G1_i*(1-(v+1)/n) + I[N-n]       
        G1[N-1] = G1_i*np.sqrt(delta)
    return(G1)