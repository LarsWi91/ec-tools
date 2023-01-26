import os
import sys
import time
import csv
import numpy as np
from scipy.integrate import cumulative_trapezoid


script_dir = os.path.dirname(__file__)
mymodule_dir1 = os.path.join(script_dir, "../test/") 
mymodule_dir2 = os.path.join(script_dir, "../ec_tools/semi_integration/")
sys.path.append(mymodule_dir1)
sys.path.append(mymodule_dir2)

import hemispherical_electrode as he

# clear old pythran code
# import pythran_cleanup as pc
# pc.clean_pytran(mymodule_dir2)

import semi_integration as si
# clear old pythran code
si.clean_pytran(mymodule_dir2)

#si.pythranizing("all")

#import R1_tr as R1
#import FRLT_tr as FRLT 
import G1_tr as G1
#time.sleep(5)
print('\nall imported?')

N_list = [7500,10000,12500,15000,20000]

# Initialize
t_G1 = np.zeros(np.size(N_list))
e_G1_max = np.zeros(np.size(N_list))
e_rel_G1_max = np.zeros(np.size(N_list))

# Print header
print("\n Gruenwald Algorithm\n")
print(" N      |  t (s) | max abs err | max rel err")

for i in range(0, np.size(N_list)):

    # No. of Elems
    N = N_list[i]

    # generate test potential
    [t, I] = he.current_hemispherical1(N_max=N)
    # with default values
    # run first calculation twice
    if i == 0:
        G1.semi_integration(I, t)
             
    # calculation of alg
    t_i = time.time()
    d_G1 =G1.semi_integration(I, t)
    t_G1[i] = time.time() - t_i

    d_G1 = d_G1[:-1]

    # Reference values
    d_ref = cumulative_trapezoid(I, t)

    # absolute error
    e_G1 = np.abs(d_G1 - d_ref)
    e_G1_max[i] = np.max(e_G1)

    # relative error
    e_rel_G1 = e_G1 / (np.abs(d_ref))
    e_rel_G1_max[i] = np.max(e_rel_G1)

    # Results
    print(
        "{:.1e}".format(N),
        "| {:6.3}".format(t_G1[i]),
        "|    {:.2e}".format(e_G1_max[i]),
        "| {:.2e}".format(e_rel_G1_max[i]),
    )
