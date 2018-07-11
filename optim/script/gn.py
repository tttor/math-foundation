# https://stackoverflow.com/questions/29699057/implementation-of-the-gauss-newton-method-from-wikipedia-example
import scipy
import numpy as np
from numpy.linalg import inv
import math
import scipy.misc

#from matplotlib import pyplot as plt, cm, colors

S = [0.038,0.194,.425,.626,1.253,2.500,3.740]
rate = [0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317]
iterations = 5
rows = 7
cols = 2

B = np.matrix([[.9],[.2]]) # original guess for B
print(B)

Jf = np.zeros((rows,cols)) # Jacobian matrix from r
r = np.zeros((rows,1)) #r equations


def model(Vmax, Km, Sval):
   return ((Vmax * Sval) / (Km + Sval))

def partialDerB1(B2,xi):
   return round(-(xi/(B2+xi)),10)

def partialDerB2(B1,B2,xi):
   return round(((B1*xi)/((B2+xi)*(B2+xi))),10)

def residual(x,y,B1,B2):
   return (y - ((B1*x)/(B2+x)))

#
for _ in xrange(iterations):

   sumOfResid=0
   #calculate Jr and r for this iteration.
   for j in xrange(rows):
      r[j,0] = residual(S[j],rate[j],B[0],B[1])
      sumOfResid += (r[j,0] * r[j,0])
      Jf[j,0] = partialDerB1(B[1],S[j])
      Jf[j,1] = partialDerB2(B[0],B[1],S[j])

   Jft =  Jf.T
   B -= np.dot(np.dot( inv(np.dot(Jft,Jf)),Jft),r)

   print B
