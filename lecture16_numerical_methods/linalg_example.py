import numpy as np
import time

n = 100
A = np.random.rand(n,n)
b = np.random.rand(n,1)

t0 = time.time()
x = np.linalg.solve(A,b)
tsolve = time.time() - t0

t1 = time.time()
x = np.dot(np.linalg.inv(A),b)
tinverse = time.time() - t1


print 'Time for solve() : ' + str(tsolve)
print 'Time for A^-1*b  : ' + str(tinverse)
print 'The Solve function is ' + str(tinverse/tsolve) + 'times faster'
