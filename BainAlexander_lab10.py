###Lab 10 
import numpy 

def make_tridiagonal(N,b,d,a):
    a = numpy.eye(N,N,0)*d + numpy.eye(N,N,1)*a +  numpy.eye(N,N,-1)*b
    return a 

A = make_tridiagonal(5,3,1,5)
print(A)