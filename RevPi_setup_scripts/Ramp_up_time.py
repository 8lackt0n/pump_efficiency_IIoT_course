
import Modbus_Functions as mb
import time
#import matplotlib.pyplot as plt
import numpy as np

#%%
mb.manual_mode()
time.sleep(1)

t  = np.array([1])
s1 = np.array([1])
s2 = np.array([1])
p1 = np.array([1])
p2 = np.array([1])
o1 = np.array([1])
o2 = np.array([1])

mb.write_data(1, 0)
mb.write_data(3, 0)
print('Speed set to 0')
print('Waiting for ramp down')
time.sleep(10)

mb.write_data(1, 1500)
mb.write_data(3, 1500)
print('Speed set to 1500')
print('Ramping up and measuring data')

t_start = time.time()
t_end = time.time() + 10
while time.time() < t_end:
    t  = np.append(t, time.time()-t_start)
    s1 = np.append(s1, round(mb.read_data(1), 2))
    s2 = np.append(s2, round(mb.read_data(7), 2))
    p1 = np.append(p1, round(mb.read_data(3), 2))
    p2 = np.append(p2, round(mb.read_data(9), 2))
    o1 = np.append(o1, round(mb.read_data(5), 2))
    o2 = np.append(o2, round(mb.read_data(11), 2))
    time.sleep(0.1)

mb.write_data(1, 0)
mb.write_data(3, 0)
print('Speed set to 0')
print('Ramping down and measuring data')

t_end = time.time() + 10
while time.time() < t_end:
    t  = np.append(t, time.time()-t_start)
    s1 = np.append(s1, round(mb.read_data(1), 2))
    s2 = np.append(s2, round(mb.read_data(7), 2))
    p1 = np.append(p1, round(mb.read_data(3), 2))
    p2 = np.append(p2, round(mb.read_data(9), 2))
    o1 = np.append(o1, round(mb.read_data(5), 2))
    o2 = np.append(o2, round(mb.read_data(11), 2))
    time.sleep(0.1)

t  = np.delete(t, 0)
s1 = np.delete(s1, 0)
s2 = np.delete(s2, 0)
p1 = np.delete(p1, 0)
p2 = np.delete(p2, 0)
o1 = np.delete(o1, 0)
o2 = np.delete(o2, 0)

mb.auto_mode()

data_out = np.array([s1, p1, o1, s2, p2, o2, t]).T

np.savetxt("Ramp_up_time.csv", data_out, delimiter=",")
