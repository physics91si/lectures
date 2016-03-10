import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt


def dx(x,t):
    m = 1
    k = 1
    c = -.1
    dx1 = x[1]
    dx2 = 1.0/m * (-k*x[0] + c*x[1])
    return [dx1,dx2]



IC = [2,0]
time = np.linspace(0,100,200)

x = scipy.integrate.odeint(dx,IC,time)

plt.plot(time,x[:,0])
plt.show()
