###Lab 10 

###Part 1 ###
import numpy as np #importing librarys

#this is the function that creates the requested array, it takes the arguments
# N = array size in collumns and rows 
#b = to the values in the diagonal one down from the central diagonal
#d = to the valeus in the central diagonal
# b - to the values in the diagonal one above the central diagonal
def make_tridiagonal(N,b,d,a): 
    #np.eye creates a function of N by N size that assigns a diagonal values of 1
    #and the others 0, the third argument is the specific diagonal, with 0 being the central one
    # the number assigned to it is the # of diagonals either above or below the central one you are 
    #trying to add 1's too, with -# being below and +# being above the central diagonal
    #we multiply each array by the value we want each diagonal to be
    #then we add the arrays and return the answer
    arr = np.eye(N,N,0)*d + np.eye(N,N,1)*a +  np.eye(N,N,-1)*b
    return arr 
#this just calls the function as A and then we print it after
A = make_tridiagonal(5,3,1,5)
print(A)

### Part 2 ###

from matplotlib import pyplot as plt
#this is a function that returns the initial condition
#it takes the arguments, sigma, K and x
def make_initialcond(sigma,K,x):
    #the initial condition can be taken as the waveform below
    a = np.exp(-((x)**2)/(2*sigma**2))*np.cos(K*x)
    return a 
#these are constants given
L =5
N=500
#this creates the spatial grid from the value of -L/2 to L/2 with N even steps
xi = np.linspace(L/2,L/2+5,N) -5
#this calls the function with the given paramaters
Aofx0 = make_initialcond(sigma = 0.2,K=35,x=xi)

#this plots the values of A(x,0) against the values of Xi and returns the graph
plt.plot(xi,Aofx0)
plt.xlabel('Values of X')
plt.ylabel('a(x,0) values')
plt.title('a(x,0) vs. X')
plt.show()


#Part 3


def spectral_radius(A):
    eigval, eigvec = np.linalg.eig(A)
    eigvalabs = map(abs,eigval)
    eigvalabsmax = max(eigvalabs)
    return (eigvalabsmax)

print(spectral_radius(A))