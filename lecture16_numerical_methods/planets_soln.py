import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def yp(y,t):
    # Write your derivative function for the update of motion
    musun = 1.32712440018E+11
    muearth = 398600.440

    yp = np.zeros(12,)  # initializing it, add in values for the 12 derivatives

    yp[0:6] = y[6:]

    r = -y[0:3] + y[3:6]

    yp[6:9] = musun * r/(np.linalg.norm(r)**3)
    yp[9:12] = muearth * (-r)/(np.linalg.norm(r)**3)

    return yp


# Initial position of sun  (units [km] in x,y,z)
rsun0 = np.array([-5.974106204422903E+05,-1.019805321061417E+04,2.020985344984197E+03])
# Initial velocity of sun (units [km] in x,y,z)
vsun0 = np.array([+3.498413911739246E-03,-1.024683372409892E-02,-6.142164304661366E-05])

# Initial position of sun  (units [km] in x,y,z)
# Initial velocity of sun (units [km] in x,y,z)
rearth0 = np.array([-9.996242777557115E+07, -1.137530941203014E+08, 5.721934792555869E+03])
vearth0 = np.array([+2.196147673706242E+01,-1.971384071968642E+01, 1.206052479401087E-03])

tinitial = 0
tfinal = 365*24*60*60  # number seconds in a year

# Your state is a combination of the positions and velocities of the earth and sun!
# It is 12 units in size
initial_state = np.concatenate([rearth0,rsun0,vearth0,vsun0])

# Solve your ODE here
t = np.linspace(tinitial,tfinal,10000)
y = odeint(yp,initial_state,t)


# Code for plotting the orbits, it assumes the output from your function as y
# Uncomment to use once you have generated data

f = plt.figure()
ax = f.add_subplot(111,projection='3d')
ax.set_aspect('equal')
plt.plot(y[:,0], y[:,1],-y[:,2])
plt.plot(y[:,3], y[:,4],-y[:,5],'.')
#plt.gca().set_aspect('equal')
plt.show()
