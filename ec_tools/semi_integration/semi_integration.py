r"""
Calls a semi-integration (v=-0.5) or semi-differentiation (v=0.5) method,
including native implementation or with speed up.
Available algorithms (alg=):
    "FRLT"      Fast Riemann-Liouville transformation
    "G1"        Gruenwald
    "R1"        Riemann and Liouville
Available settings (set_flag=):
    "py"        python implementation
    "jit"       numba just in time
"""


from transonic import jit, boost,set_compile_at_import
from ec_tools.semi_integration import G1 as G1
@jit(backend = 'numba')            
def alg(I: "float[:]",t: "float[:]", v:float =-0.5):
    return G1.semi_integration(I,t)

def semi_integration(I,t,v=-0.5, alg ="FRLT", set_flag="transonic"):

    if alg == "FRLT":
        delta_x = t[1] - t[0]
        if set_flag == "py":
            import FRLT as FRLT
            res = FRLT.semi_integration(I, delta_x=delta_x)
        elif set_flag == "jit":
            # import FRLT_nu as FRLT
            # res = FRLT.semi_integration(I, delta_x=delta_x)
            from numba import jit
            import FRLT as FRLT
            mysetup = jit(FRLT.semi_integration)
            res = mysetup(I, delta_x=delta_x)
        elif set_flag == "transonic":
            from . import FRLT_tr as FRLT
            res = FRLT.semi_integration(y=I, delta_x=delta_x)
        else:
            print("\nNo matching setting with choosen FRLT algorithm")
            res = "NaN"

    elif alg == "G1":
        delta_x = t[1] - t[0]
        if set_flag == "py":
            import G1 as G1
            res = G1.semi_integration(I, t)
        elif set_flag == "jit":
            from numba import jit 
            import G1 as G1
            mysetup = jit(G1.semi_integration)
            res = mysetup(I, t)
        elif set_flag == "transonic":
            # from . import G1_tr as G1
            # res = G1.semi_integration(I, t)

            from . import G1 as G1
            from transonic import jit, boost,set_compile_at_import
            #set_compile_at_import(True)
            # @boost
            @jit(backend = 'numba')            
            def alg(I: "float[:]",t: "float[:]", v:float =-0.5):
                return G1.semi_integration(I,t)

            res = alg(I,t) 

        else:
            print("\nNo matching setting with choosen G1 algorithm")
            res = "NaN"

    elif alg == "R1":
        delta_x = t[1] - t[0]
        if set_flag == "py":
            import R1 as R1
            res = R1.semi_integration(I, t)
        elif set_flag == "jit":
            # import R1_nu as R1
            # res = R1.semi_integration(I, t)
            from numba import jit 
            import R1 as R1
            mysetup = jit(R1.semi_integration)
            res = mysetup(I, t)

        elif set_flag == "transonic":
            import R1_tr as R1
            res = R1.semi_integration(I, t)
        else:
            print("\nNo matching setting with choosen R1 algorithm")
            res = "NaN"

    else:
        print("\nNo matching algorithm found with these flags")
        res = "NaN"
    return res


import os
import shutil
# clean old pythran code
def clean_pytran(dir):
    if os.path.exists(''.join([dir,"/__pythran__"])):
        print(''.join(["Previous pythran code cleaned in ",dir]))
        shutil.rmtree("../ec_tools/semi_integration/__pythran__")
        
    else:
        print(''.join(["No pythran code found to clean in ", dir]))
    return()

# pre-import alg for pythran
def pythranizing(alg_name):
    if alg_name == "G1":
        import G1_tr as G1
    elif alg_name == "R1":
        import R1_tr as R1
    elif alg_name == "FRLT":
        import FRLT_tr as FRLT
    elif alg_name == "all":
        import G1_tr as G1
        import R1_tr as R1
        import FRLT_tr as FRLT
    else:
        print('No algorithm packages found to import')
    return('packages imported')
