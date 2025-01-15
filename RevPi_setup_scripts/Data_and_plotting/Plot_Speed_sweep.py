import numpy as np
import matplotlib.pyplot as plt

#%%
data = np.loadtxt("Speed_sweep.csv", delimiter=",", dtype=float)

#%%
plt.figure(1)
plt.plot(data[:,0], data[:,1], label='Pump1 power')
plt.plot(data[:,3], data[:,4], label='Pump2 power')

plt.title('Power consumption at different pump speeds')
plt.xlabel('Pump speed [rpm]')
plt.ylabel('Power [W]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(2)
plt.plot(data[:,0], data[:,2], label='Pump1 outflow')
plt.plot(data[:,3], data[:,5], label='Pump2 outflow')

plt.title('Waterflow at different pump speeds')
plt.xlabel('Pump speed [rpm]')
plt.ylabel('Outflow [m^3/h]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(2)
plt.plot(data[:,0], data[:,2]/data[:,1], label='Pump1')
plt.plot(data[:,3], data[:,5]/data[:,4], label='Pump2')

plt.title('Waterflow pr. watt at different pump speeds')
plt.xlabel('Pump speed [rpm]')
plt.ylabel('Outflow pr. power [m^3/Wh]')
plt.legend()
plt.grid()
plt.show()