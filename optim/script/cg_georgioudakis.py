#!/usr/bin/env python3
# http://georgioudakis.com/blog/python/conjugate_gradient.html
# https://en.wikipedia.org/wiki/Conjugate_gradient_method

import numpy as np

def main():
    A = np.matrix([[4.0, 1.0], [1.0, 3.0]])
    b = np.matrix([[1.0], [2.0]])
    x0 = np.matrix([[0.0], [0.0]])

    x = conjugate_gradient(A, b, x0)
    print(x)

def conjugate_gradient(A, b, x0, TOLERANCE = 1.0e-10, MAX_ITERATIONS = 100):
    """
    A function to solve [A]{x} = {b} linear equation system with the
    conjugate gradient method.

    More at: http://en.wikipedia.org/wiki/Conjugate_gradient_method

    ========== Parameters ==========
    A : array
        A real symmetric positive definite matrix.
    b : vector
        The right hand side (RHS) vector of the system.
    x0 : vector
        The starting guess for the solution.
    MAX_ITERATIONS : integer
        Maximum number of iterations. Iteration will stop after maxiter
        steps even if the specified tolerance has not been achieved.
    TOLERANCE : float
        Tolerance to achieve. The algorithm will terminate when either
        the relative or the absolute residual is below TOLERANCE.
    """

    #   Initializations
    x = x0
    r0 = b - np.dot(A, x)
    p = r0

    #   Start iterations
    for i in range(MAX_ITERATIONS):
        a = float(np.dot(r0.T, r0)/np.dot(np.dot(p.T, A), p))
        x = x + p*a

        ri = r0 - np.dot(A*a, p)
        print ( 'i=%d --> norm(ri)=%f' %(i, np.linalg.norm(ri)) )

        if np.linalg.norm(ri) < TOLERANCE:
            return x

        b = float(np.dot(ri.T, ri)/np.dot(r0.T, r0))
        p = ri + b * p
        r0 = ri

    return x

if __name__ == '__main__':
    main()
