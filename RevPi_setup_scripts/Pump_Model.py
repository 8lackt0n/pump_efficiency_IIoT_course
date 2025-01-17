#%% Drawing
#
#    Grid          Drive 1        Motor 1       Turbine 1
#    _____
#   /     \        ________       ________       ________
#  /       \      |        |     |        |     |        |
# |    ~    |-----|   D1   |-----|   M1   |-----|   T1   |---
#  \       /      |________|     |________|     |________|
#   \_____/            |              |              |
#            P_in      |     P_e      |     P_m      |     P_r
#            V_in      |     T_e      |     T_m      |     Q_out
#            I_in      |     w_e      |     w_m      |     p_out
#                      |              |              |
#%% Importing packages
#import numpy as np
#import math as m
#import matplotlib.pyplot as plt

#%% Input variables
# w_s_rpm = np.linspace(0, 1500, 1501, dtype=int) # [rpm] speed target
# h       = 2/1 # [m] (0-2) height of water in the tank

#%%
def Pump_model_simulation(w_s_rpm, h):
    #%% Basic variables
    pi    = 3.141592653589793
    sqrt3 = 1.7320508075688772
    
    #%% Grid Variables
    V_in = 400 # [V] Voltage
    f    = 50  # [Hz] frequency
    
    #%% Machine variables
    P   = 4             # [] number of poles of the induction machine
    p   = P/2           # [] number of pole pairs of the induction machine
    n_s = f*60/p        # [rpm] synchronous speed
    n_n = 1470          # [rpm] nominel speed
    s   = (n_s-n_n)/n_s # [] slip
    #PF  = 0.82
    
    #%% Pump/pipe variables
    l   = 20   # [m] Lenght of the pipe
    r   = 5e-2 # [m] Radius of pipe
    eta = 1e-3 # [Pa*s] fluid viscusity
    J   = 5    # [kg*m^2] Inertia of the turbine

    #%% Speeds
    w_s = (w_s_rpm*pi)/(30) # [rad/s]
    
    w_m_rpm = (1-s)*w_s_rpm   # [rpm] mechanical speed (rotor speed)
    w_m = (w_m_rpm*pi)/(30) # [rad/s]
    
    w_e_rpm = (P/2)*w_s_rpm   # [rpm] electrical speed (speed of the rotating electircal field)
    w_e   = w_e_rpm*(pi/30) # [rad/s]
    
    #%% Pump mechanical parameters (turbine output)
    # Physical variables
    Q_out = w_m/189                       # [m^3/s] outflow of water from the tank
    p_out = (8*Q_out*eta*l)/(pi*(r**4)) # [Pa] preasure
    
    #P_turb = p_out*Q_out # [W] Turbine power
    
    #%% Motor Mechanical parameters (motor output)
    T_m = h*17.87 # [Nm]
    #P_m = T_m*w_m # [W]
    
    #%% Motor electrical parameters (drive output)
    T_e = T_m-J*(w_s-w_m)
    P_e = T_e*w_e
    
    I_e = P_e/(sqrt3*V_in)
    
    #%% Drive input parameters
    I_in = I_e*1.05
    
    #P_in = sqrt3*V_in*I_in
    
    return V_in, I_in, P_e, w_e, Q_out, p_out, w_m #, T_M

'''
#%% Efficiencies
eta_D1 = P_e/P_in
eta_M1 = P_m/P_e
eta_T1 = P_turb/P_m

#%%
plt.figure(1)
plt.plot(w_m_rpm, eta_D1*100, 'r-', label='Drive efficiency')
plt.plot(w_m_rpm, eta_M1*100, 'g-', label='Motor efficiency')
plt.plot(w_m_rpm, eta_T1*100, 'b-', label='Turbine efficiency')
plt.plot(w_m_rpm, (eta_D1*eta_M1*eta_T1)*100, 'm-', label='Total efficiency')

plt.xlabel('Speed setpoint')
plt.ylabel('Efficiency [%]')
plt.title('System efficiency')

plt.legend()
plt.grid()
plt.show()
'''