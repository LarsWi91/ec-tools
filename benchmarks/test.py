import os
import sys
import time
import numpy as np
from transonic import boost,jit

script_dir = os.path.dirname(__file__)
mymodule_dir1 = os.path.join(script_dir, "../test/") 
mymodule_dir2 = os.path.join(script_dir, "../ec_tools/semi_integration/")
sys.path.append(mymodule_dir1)
sys.path.append(mymodule_dir2)

import hemispherical_electrode as he
import G1 as G1

def my_log(b):
    return np.log(b)


@jit(backend = 'numba')
def func(b):
    s = np.max((my_log(b)))
    return s 

#@jit(backend = 'numba')
# def semi_integration(I: "float[:]",t: "float[:]", v:float =-0.5):

#     # (equidistant) time step
#     delta = t[1]-t[0]
#     # No. of steps
#     N_max = I.size
#     # initialize with zeros
#     G1 = np.zeros(N_max)
#     for N in range(1,N_max+1):
#         # value for n = N with w0 = 1
#         G1_i = I[0]; 
#         #      go from N to 0
#         for n in range(N-1,0,-1):
#             G1_i = G1_i*(1-(v+1)/n) + I[N-n]       
#         G1[N-1] = G1_i*np.sqrt(delta)
#     return(G1)

@jit(backend = 'numba')
def alg(I: "float[:]",t: "float[:]", v:float =-0.5):
    return G1.semi_integration(I,t,v)

# print(func(1000))


N = 1000
[t, I] = he.current_hemispherical1(N_max=N)

t_i = time.time()
d_res =alg(alg(I,t),t)

# d_res = semi_integration(semi_integration(I,t),t)
print(time.time() - t_i)