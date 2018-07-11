#!/usr/bin/env python3
# http://ikuz.eu/2015/04/15/the-concept-of-conjugate-gradient-descent-in-python/

import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def main():
    A = np.matrix([[3.0, 2.0], [2.0, 6.0]])
    b = np.matrix([[2.0], [-8.0]])  # we will use the convention that a vector is a column vector
    c = 0.0

    x1, x2, zs = bowl(A, b, c)
    contoursteps(x1, x2, zs)

    # steps = steepest_descent(A, b)
    # contoursteps(x1, x2, zs, steps)

    # steps = steepest_descent_with_fixed_learning_rate(A, b, alpha=0.12)
    # contoursteps(x1, x2, zs, steps)

    steps = conjugate_gradient(A, b)
    contoursteps(x1, x2, zs, steps)

def fn(x, A, b, c):
    return float(0.5 * x.T * A * x - b.T * x + c)

def bowl(A, b, c):
    fig = plt.figure(figsize=(10,8))
    qf = fig.gca(projection='3d')
    size = 20
    x1 = list(np.linspace(-6, 6, size))
    x2 = list(np.linspace(-6, 6, size))
    x1, x2 = np.meshgrid(x1, x2)
    zs = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.matrix([[x1[i,j]], [x2[i,j]]])
            zs[i,j] = fn(x, A, b, c)
    qf.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)

    plt.savefig('./plot/bowl.png',dpi=300,format='png',bbox_inches='tight');
    plt.close(fig)

    return x1, x2, zs

def contoursteps(x1, x2, zs, steps=None):
    fig = plt.figure(figsize=(6,6))
    cp = plt.contour(x1, x2, zs, 10)
    plt.clabel(cp, inline=1, fontsize=10)
    if steps is not None:
        steps = np.matrix(steps)
        plt.plot(steps[:,0], steps[:,1], '-o')
    plt.savefig('./plot/contour.png',dpi=300,format='png',bbox_inches='tight');
    plt.close(fig)

def steepest_descent_with_fixed_learning_rate(A, b, alpha):# aka gradient descent
    x = np.matrix([[-2.0],[-2.0]])
    steps = [(-2.0, -2.0)]
    i = 0
    imax = 10000
    eps = 0.01

    r = b - A * x
    delta = r.T * r
    delta0 = delta

    while i < imax and delta > eps**2 * delta0:
        x = x + alpha * r
        steps.append((x[0,0], x[1,0]))  # store steps for future drawing

        r = b - A * x
        delta = r.T * r

        i += 1

    return steps

def steepest_descent(A, b):
    # init
    x = np.matrix([[-2.0],[-2.0]])
    steps = [(-2.0, -2.0)]
    i = 0
    imax = 10
    eps = 0.01

    r = b - A * x # residual, ie the direction of steepest descent.
    delta = r.T * r
    delta0 = delta

    while i < imax and delta > eps**2 * delta0:
        alpha = float(delta / (r.T * (A * r))) # how far along that direction we need to go?.

        x = x + alpha * r
        steps.append((x[0,0], x[1,0]))  # store steps for future drawing

        r = b - A * x # repeat finding the direction
        delta = r.T * r

        i += 1

    return steps

def conjugate_gradient(A, b):
    x = np.matrix([[-2.0],[-2.0]])
    steps = [(-2.0, -2.0)]
    i = 0
    imax = 10
    eps = 0.01

    r = b - A * x # r: residual
    d = r # d: conjugate vectors, which we call directions.
    delta = r.T * r
    delta0 = delta

    while i < imax and delta > eps**2 * delta0:
        alpha = float(delta / float(d.T * (A * d)))

        x = x + alpha * d
        steps.append((x[0, 0], x[1, 0]))

        r = b - A * x

        deltaold = delta
        delta = r.T * r

        # \beta steered us to the conjugate direction.
        # beta = -float((r.T * A * d) / float(d.T * A * d))
        beta = float(delta / float(deltaold)) # simplified version

        d = r + beta * d

        i += 1

    return steps

if __name__ == '__main__':
    main()
