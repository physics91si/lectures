from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dy(y,x):
    k = .5
    c = -.1
    yp1 = y[1]
    yp2 = -k*y[0] + c*y[1]
    return [yp1,yp2]

def solve():
    IC = [5,0]

    t = np.linspace(0,100,100)
    x = odeint(dy,IC,t)

    plt.plot(t,x[:,1],'b-',linewidth=1.5)
    plt.show()


solve()
