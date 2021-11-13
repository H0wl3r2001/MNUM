import math
import numpy as np
#the function to be integrated:
def f(x):
    return x**4
 
#define a function to do integration of f(x) btw. a and b:
def trap(f, n, a, b):
    h = (b - a) / float(n)
    intgr = 0.5 * h * (f(a) + f(b))
    for i in range(1, int(n)):
        intgr = intgr + h * f(a + i * h)
    return intgr
 
#real_v = 20000


def simps(f,a,b,N=50):
    '''Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.

    Examples
    --------
    >>> simps(lambda x : 3*x**2,0,1,10)
    1.0
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

St = trap(f,10, 0, 10)
Ss = simps(f,0, 10, 10)

S1t = trap(f,20, 0, 10)
S1s = simps(f,0, 10, 20)

S2t = trap(f,40, 0, 10)
S2s = simps(f,0, 10, 40)

print("QCtrpz: ")
print((S1t-St)/(S2t-S1t), '\n')

print("Epsilon_trpz: ")
print((S2t-S1t)/(2**2-1))


print("QCsps: ")
print((S1s-Ss)/(S2s-S1s), '\n')

print("Epsilon_sps: ")
print((S2s-S1s)/(2**4-1))