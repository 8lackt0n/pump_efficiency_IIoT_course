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

#%%
plt.figure(2)
plt.plot(data[T100,1], data[T100,2]/100*data[T100,1]/100*5500, 'r-', label='Motor')
plt.plot(data[T100,1], data[T100,4], 'g-', label='Motor loss')
plt.plot(data[T100,1], data[T100,5], 'b-', label='Drive loss')
plt.plot(data[T100,1], data[T100,7], 'm-', label='Total loss')

plt.title('Motor power and losses at 100% torque')
plt.xlabel('Pump speed [%]')
plt.xlim([min(data[:,1]),max(data[:,1])])
plt.ylabel('Power [W]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(3)
plt.plot(data[T50,1], data[T50,2]/100*data[T50,1]/100*5500, 'r-', label='Motor')
plt.plot(data[T50,1], data[T50,4], 'g-', label='Motor loss')
plt.plot(data[T50,1], data[T50,5], 'b-', label='Drive loss')
plt.plot(data[T50,1], data[T50,7], 'm-', label='Total loss')

plt.title('Motor power and losses at 50% torque')
plt.xlabel('Pump speed [%]')
plt.xlim([min(data[:,1]),max(data[:,1])])
plt.ylabel('Power [W]')
plt.legend()

plt.grid()
plt.show()

#%%
plt.figure(4)
plt.plot(data[T25,1], data[T25,2]/100*data[T25,1]/100*5500, 'r-', label='Motor')
plt.plot(data[T25,1], data[T25,4], 'g-', label='Motor loss')
plt.plot(data[T25,1], data[T25,5], 'b-', label='Drive loss')
plt.plot(data[T25,1], data[T25,7], 'm-', label='Total loss')

plt.title('Motor power and losses at 25% torque')
plt.xlabel('Pump speed [%]')
plt.xlim([min(data[:,1]),max(data[:,1])])
plt.ylabel('Power [W]')
plt.legend()

plt.grid()
plt.show()