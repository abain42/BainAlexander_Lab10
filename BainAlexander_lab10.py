###Lab 10 

###Part 1 ###
import numpy as np

def make_tridiagonal(N,b,d,a):
    arr = np.eye(N,N,0)*d + np.eye(N,N,1)*a +  np.eye(N,N,-1)*b
    return arr 

A = make_tridiagonal(5,3,1,5)
print(A)

### Part 2 ###

from matplotlib import pyplot as plt

def make_initialcond(sigma,K,x):
    a = np.exp(-((x)**2)/(2*sigma**2))*np.cos(K*x)
    return a 
L =5
N=500
xi = np.linspace(L/2,L/2+5,N) -5
Aofx0 = make_initialcond(sigma = 0.2,K=35,x=xi)

plt.plot(xi,Aofx0)
plt.xlabel('Values of X')
plt.ylabel('a(x,0) values')
plt.title('a(x,0) vs. X')
plt.show()


