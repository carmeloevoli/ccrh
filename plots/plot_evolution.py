#!/bin/bash/python
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import numpy as np

# begin plot style options
rc('text', usetex=True)
rc('font', family='serif')
rc('font', serif='Helvetica Neue')
rc('xtick', labelsize=18)
rc('ytick', labelsize=18)
rcParams['legend.numpoints'] = 1
rcParams['lines.linewidth'] = 3

fig = plt.figure(figsize=(8.1, 7.8))
ax = fig.add_subplot(1, 1, 1)

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(1.5)

ax.minorticks_on()
ax.tick_params('both', length=15, width=1.5, which='major', pad=6)
ax.tick_params('both', length=10, width=1.3, which='minor', pad=6)

plt.xticks(size=28)
plt.yticks(size=28)
# end plot style options

def read_file(datafile,xcol,ycol):
    x = []
    y = []
    f = open(datafile,'r')
    header = f.readline()
    for line in f:
        line = line.strip()
        columns = line.split()
        x.append(float(columns[xcol]))
        y.append(float(columns[ycol]))
    f.close()
    data=[]
    data.append(np.array(x))
    data.append(np.array(y))
    return data

plt.yscale('log')
#plt.xscale('log')

plt.xlabel(r'$z$', size=28)
plt.ylabel(r'$\Lambda_{\rm ion}$ [Myr$^{-1}$]', size=28)

plt.axis()#[1e-3,10,1e-2,1e5],interpolation='none')

data = read_file('output/test_with_CR_100_keV_igm.txt',0,6)
plt.plot(data[0],data[1],'b',label='Ph-Ion')

data = read_file('output/test_with_CR_100_keV_igm.txt',0,7)
plt.plot(data[0],data[1],'b--',label='CR-Ion')

data = read_file('output/test_with_CR_100_keV_igm.txt',0,9)
plt.plot(data[0],data[1],'r',label='Ph-Heating')

data = read_file('output/test_with_CR_100_keV_igm.txt',0,10)
plt.plot(data[0],data[1],'r--',label='CR-Heating')


#plt.text(16.5,10,'Coulomb',size=20,rotation=65)

#plt.ylim()[1e-7,1e-2])

#plt.legend(loc='upper right')

#plt.show()

plt.savefig('photo_ionization_rate.pdf', format='pdf', bbox_inches='tight', dpi=300)