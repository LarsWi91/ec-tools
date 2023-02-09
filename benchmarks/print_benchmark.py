import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define FIGNAME
if len(sys.argv) == 2:
    FIGNAME = sys.argv[1]
else:
    FIGNAME = 'benchmark'

# for draft mode set False
save_figs = True

# plot size
plt.rcParams['figure.figsize'] = [10, 8]

# Save figures as png? 
save_figs = True

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

# Column entries
col_lst = ['t_FRLT','e_FRLT_max','e_rel_FRLT_max',
           't_G1','e_G1_max','e_rel_G1_max',
           't_R1','e_R1_max', 'e_rel_R1_max']
# Methods (short)
mtd_lst = ['py','nu','tr','ru']
# Methods (long)
method_lst = ['Pyhton','Numba','Transonic','Rust']

df = pd.DataFrame()
df['N'] = df_py['N']
for i in range(len(col_lst)):
    ## import from
    # python
    df = df.join(df_py[col_lst[i]])
    df = df.rename(columns={col_lst[i]:''.join([col_lst[i],'_',mtd_lst[0]])})
    # numba
    df = df.join(df_nu[col_lst[i]])
    df = df.rename(columns={col_lst[i]:''.join([col_lst[i],'_',mtd_lst[1]])})
    # transonic
    df = df.join(df_tr[col_lst[i]])
    df = df.rename(columns={col_lst[i]:''.join([col_lst[i],'_',mtd_lst[2]])})
    # rust
    df = df.join(df_ru[col_lst[i]])
    df = df.rename(columns={col_lst[i]:''.join([col_lst[i],'_',mtd_lst[3]])})

## create lists for times and errors
# Times
t_lst = []        # (short)
t_method_lst = [] # (long)
for i in range(0,len(col_lst),3):
    for j in range(len(mtd_lst)):
        t_lst.append(''.join([col_lst[i],'_',mtd_lst[j]]))
        t_method_lst.append(''.join([col_lst[i],' ',method_lst[j]]))

# (absolute) errors
e_lst = []        # (short)
e_method_lst = [] # (long)
for i in range(1,len(col_lst),3):
    for j in range(len(mtd_lst)):
        e_lst.append(''.join([col_lst[i],'_',mtd_lst[j]]))
        e_method_lst.append(''.join([col_lst[i],' ',method_lst[j]]))

# relative errors
e_rel_lst = []        # (short)
e_rel_method_lst = [] # (long)
for i in range(2,len(col_lst),3):
    for j in range(len(mtd_lst)):
        e_rel_lst.append(''.join([col_lst[i],'_',mtd_lst[j]]))
        e_rel_method_lst.append(''.join([col_lst[i],' ',method_lst[j]]))

## Define colors for differen algorithms 
#   FRTLT , G1 , R1
col = ['g','b','r']
# Define symbols for different approachees
#       py , nu , tr , ru 
sym = ['.:','x:','+:','d:']

# create list of all variations
sym_lst = []
for i in range(len(col)):
    for j in range(len(sym)):
        sym_lst.append(''.join([col[i],sym[j]]))

print(FIGNAME)

## Plot performance test for each alg and each approach
fig = plt.figure()
ax = plt.subplot(111)
   
for i in range(len(t_lst)):   
    ax.semilogy(df_py['N'], df[t_lst[i]],
                sym_lst[i],
                label=t_method_lst[i])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.8])

plt.title('Time performance test \nfor different alg by different approach')
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))

plt.xlabel('No. of Elems [-]')
plt.ylabel('$\it{t}$ / s')
plt.grid(visible=True)

if save_figs:
    print('save fig')
    plt.savefig(''.join(['images/',FIGNAME,'_time.png']), dpi=600)

## Plot performance test for each alg and each approach
plt.rcParams['figure.figsize'] = [10, 8]
fig = plt.figure()
ax = plt.subplot(111)
   
for i in range(len(t_lst)):   
    ax.semilogy(df_py['N'], df[e_lst[i]],
                sym_lst[i],
                label=e_method_lst[i])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.8])

plt.title('Absolute error of performance test \nfor different alg by different approach')
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))

plt.xlabel('No. of Elems [-]')
plt.ylabel('absolute error')
plt.grid(visible=True)

if save_figs:
    print('save fig')
    plt.savefig(''.join(['images/',FIGNAME,'_abs_err.png']), dpi=600)

## Plot performance test for each alg and each approach
plt.rcParams['figure.figsize'] = [10, 8]
fig = plt.figure()
ax = plt.subplot(111)
   
for i in range(len(t_lst)):   
    ax.semilogy(df_py['N'], df[e_rel_lst[i]],
                sym_lst[i],
                label=e_rel_method_lst[i])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.8])

plt.title('Relative error of performance test \nfor different alg by different approach')
ax.legend(loc='center left',bbox_to_anchor=(1,0.5))

plt.xlabel('No. of Elems [-]')
plt.ylabel('absolute error')
plt.grid(visible=True)

if save_figs:
    print('save fig')
    plt.savefig(''.join(['images/',FIGNAME,'_rel_err.png']), dpi=600)