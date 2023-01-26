r"""
Implementation of an algorithm for 
semi-integration (v=-0.5) and semi-differentiation (v=0.5)
Riemann and Liouville semi-integration and semi-differentiation (R1)
based on
Oldham: Electrochemical Science and Technology, 2012
"""

import numpy as np


def semi_integration(I,t,v=-0.5):
    """
    TEST:
    >>> import pandas as pd
    >>> from scipy.integrate import cumulative_trapezoid
    >>> df1 = pd.read_csv('../../test/data/Testfile_1.csv')
    >>> np.allclose(semi_integration(semi_integration(df1['I'],df1['t']), df1['t'])[:-1], cumulative_trapezoid(df1['I'],df1['t']), rtol=1e-0)
    True
    >>> df2 = pd.read_csv('../../test/data/Testfile_2.csv')
    >>> np.allclose(semi_integration(semi_integration(df2['I'],df2['t']), df2['t'])[:-1], cumulative_trapezoid(df2['I'],df2['t']), rtol=1e-0)
    True
    """
    # (equidistant) time step
    delta = t[1] - t[0]
    # No. of steps
    N_max = I.size
    # initialize with zeros
    R1 = np.zeros(N_max)

    if v==-0.5:
        sqrt_d_pi = (4 / 3) * np.sqrt(delta / np.pi)
    elif v==0.5:
        sqrt_d_pi = 2 /np.sqrt(delta * np.pi)

    for N in range(1, N_max + 1):
        R1_i = 0
        for n in range(1, N):
            R1_i += I[n - 1] * (
                (N - n + 1) ** (1-v) - 2 * (N - n) ** (1-v) + (N - n - 1) ** (1-v)
            )

        R1[N - 1] = (sqrt_d_pi * (I[N - 1] + I[0] * ((1-v)*N**(-v) - N**(1-v) + (N-1)**(1-v))+ R1_i)
        )

    return R1