import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Save figures as png? 
save_figs = True

# define figure name
FIGNAME = "Benchmark_23_01_19"

## Define Filenames 
# with native python code
FILENAME_py = "results/py_benchmark_results.csv" 
# with numba
FILENAME_nu = "results/numba_benchmark_results.csv" 
# with transonic
FILENAME_tr = "results/transonic_benchmark_results.csv" 
# with native rust code
Filename_ru = "results/rust_benchmark_results.csv" 

# import python result values
df_py = pd.read_csv(FILENAME_py)

# import numba result values
df_nu = pd.read_csv(FILENAME_nu)

# import transonic result values
df_tr = pd.read_csv(FILENAME_tr)

# import rust result values
df_ru = pd.read_csv(Filename_ru)

## Plot performance test for each alg and each approach
fig = plt.figure()
ax = plt.subplot(111)

alg_list = ['G1','R1','FRLT']
app_list = ['Python','Numba','Transonic']
c_list = ['g','b','r']
sym_list = ['.:','x:','+:']

for i in range(len(alg_list)):
    ax.semilogy(df_py['N'],df_py[''.join(['t_',alg_list[i]])],
                ''.join([c_list[i],sym_list[0]]),
                label=''.join([alg_list[i],' ',app_list[0]]))
    
    ax.semilogy(df_nu['N'],df_nu[''.join(['t_',alg_list[i]])],
                ''.join([c_list[i],sym_list[1]]),
                label=''.join([alg_list[i],' ',app_list[1]]))
    
    ax.semilogy(df_tr['N'],df_tr[''.join(['t_',alg_list[i]])],
                ''.join([c_list[i],sym_list[2]]),
                label=''.join([alg_list[i],' ',app_list[2]]))


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.8])

plt.title('Time Performance Test')
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))

plt.xlabel('No. of Elems [-]')
plt.ylabel('$\it{t}$ / s')
plt.grid(visible=True)
if save_figs:
    plt.savefig(''.join(['images/',FIGNAME,'_time.png']), dpi=600)
#plt.show()