import numpy as np


def semi_integration(I, t, v=-0.5):
    # def semi_integration(I:A,t:A, v:float=-0.5):
    "\n    TEST:\n    >>> import pandas as pd\n    >>> from scipy.integrate import cumulative_trapezoid\n    >>> df1 = pd.read_csv('../../test/data/Testfile_1.csv')\n    >>> np.allclose(semi_integration(semi_integration(df1['I'],df1['t']), df1['t'])[:-1], cumulative_trapezoid(df1['I'],df1['t']), rtol=1e-12)\n    True\n    >>> df2 = pd.read_csv('../../test/data/Testfile_2.csv')\n    >>> np.allclose(semi_integration(semi_integration(df2['I'],df2['t']), df2['t'])[:-1], cumulative_trapezoid(df2['I'],df2['t']), rtol=1e-2)\n    True\n"
    # (equidistant) time step
    delta = t[1] - t[0]
    # No. of steps
    N_max = I.size
    # initialize with zeros
    G1 = np.zeros(N_max)
    for N in range(0, N_max):
        # value for n = N with w0 = 1
        G1_i = I[0]
        #      go from N to 0
        for n in range(N, 0, -1):
            G1_i = G1_i * ((v + 1) / n) + I[N - n + 1]
        G1[N] = G1_i * np.sqrt(delta)
    return G1


__transonic__ = ("0.5.1",)
