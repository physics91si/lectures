import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt


def dx(x,t):
    return x


IC = 1
t = np.linspace(0,10,100)

x = scipy.integrate.odeint(dx,IC,t)


plt.plot(t,x)

plt.show()
