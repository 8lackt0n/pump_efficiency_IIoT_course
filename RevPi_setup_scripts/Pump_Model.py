import numpy as np
import matplotlib.pyplot as plt

#%%
w_s_rpm = np.linspace(0, 1500, 1501, dtype=int) # [rpm]
s = (1500-1470)/1500
w_r_rpm = (1-s)*w_s_rpm
w_r = (w_r_rpm*np.pi)/(30) # [rad/s]
w_e = (4/2)*w_s_rpm
w   = w_e*(np.Pi/30)


#%% Pump mechanical parameters (turbine output)
# Physical variables
l   = 20   # [m] Lenght of the pipe
r   = 5e-2 # [m] Radius of pipe
eta = 1e-3 # [Pa*s] fluid viscusity

Q_out = (w_r/1041) # [m^3/s] 
p_out = (8*Q_out*eta*l)/(np.pi*(r**4))

P_turb = p_out*Q_out

#%% Motor Mechanical parameters (motor output)


T_m = 1

P_m = 1

#%% Motor electrical parameters (drive output)


T_e = 1

P_e = 1

#%% Drive input parameters


V_in = 400
I_in = 1

P_in = 1

#%%
plt.figure(1)
plt.plot(w_r_rpm, p_out)

plt.grid()
plt.show()









