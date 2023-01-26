import numpy as np
from transonic import boost,jit

# transonic def func(float[][], float[][])
# transonic def func(int[][], float[][])


def my_log(b):
    return np.log(b)


#@boost
@jit(backend = 'numba')
def func(a, b):
    return (my_log(b))

print(func(1,3))