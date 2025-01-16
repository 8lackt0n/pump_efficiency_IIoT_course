#%%
import Modbus_Functions as mb
import time
#import matplotlib.pyplot as plt
import numpy as np

#%%
mb.manual_mode()
time.sleep(1)

mb.write_data(1, 0)
mb.write_data(3, 0)
print('Speed set to 0')
print('Waiting for ramp down')
time.sleep(10)

speeds = np.arange(50, 1550, 50)

s1 = np.zeros(len(speeds))
s2 = np.zeros(len(speeds))
p1 = np.zeros(len(speeds))
p2 = np.zeros(len(speeds))
o1 = np.zeros(len(speeds))
o2 = np.zeros(len(speeds))

for i in range(len(speeds)):
    mb.write_data(1, speeds[i])
    mb.write_data(3, speeds[i])
    print(f'Speed set to {speeds[i]}')
    time.sleep(5)
    s1[i] = round(mb.read_data(1), 2)
    s2[i] = round(mb.read_data(7), 2)
    p1[i] = round(mb.read_data(3), 2)
    p2[i] = round(mb.read_data(9), 2)
    o1[i] = round(mb.read_data(5), 2)
    o2[i] = round(mb.read_data(11), 2)
    print('Values read')

mb.auto_mode()

data_out = np.array([s1, p1, o1, s2, p2, o2]).T

np.savetxt("Speed_sweep.csv", data_out, delimiter=",")
