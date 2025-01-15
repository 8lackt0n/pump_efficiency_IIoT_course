import numpy as np
import matplotlib.pyplot as plt

#%%
data = np.loadtxt("Ramp_up_time.csv", delimiter=",", dtype=float)

#%%
plt.figure(1)
plt.plot(data[:,6], data[:,0], label='Pump1')
plt.plot(data[:,6], data[:,3], label='Pump2')

plt.title('Speed ramp up and down')
plt.xlabel('Time [s]')
plt.ylabel('Speed [rpm]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(2)
plt.plot(data[:,6], data[:,1], label='Pump1')
plt.plot(data[:,6], data[:,4], label='Pump2')

plt.title('Power ramp up and down')
plt.xlabel('Time [s]')
plt.ylabel('Speed [rpm]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(2)
plt.plot(data[:,6], data[:,2], label='Pump1')
plt.plot(data[:,6], data[:,5], label='Pump2')

plt.title('outflow ramp up and down')
plt.xlabel('Time [s]')
plt.ylabel('Speed [rpm]')
plt.legend()

plt.grid()
plt.show()