import numpy as np
import matplotlib.pyplot as plt

#%%
data = np.loadtxt("Efficiency_Map_Danfoss.csv", delimiter=",", dtype=float)

T25 = np.where(data[:,2] == 25)[0]
T50 = np.where(data[:,2] == 50)[0]
T100 = np.where(data[:,2] == 100)[0]

#%%
plt.figure(1)

plt.plot(data[T25,1], data[T25,3], 'r-', label='25% Torque')
plt.plot(data[T50,1], data[T50,3], 'g-', label='50% Torque')
plt.plot(data[T100,1], data[T100,3], 'b-', label='100% Torque')

plt.title('Efficiency plot for different torque levels')
plt.xlabel('Pump speed [%]')
plt.xlim([min(data[:,1]),max(data[:,1])])
plt.ylabel('Efficiency [%]')
plt.ylim([0,100])
plt.legend()

plt.grid()
plt.show()
