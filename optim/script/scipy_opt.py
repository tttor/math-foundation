#!/usr/bin/env python3
# https://www.scipy-lectures.org/advanced/mathematical_optimization/
# pip install scipy

from scipy import optimize

def main():
    result = optimize.minimize(f, [2, -1], method="CG")
    print(result)

def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

if __name__ == '__main__':
    main()
