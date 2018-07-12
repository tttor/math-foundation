#!/usr/bin/env python3
import torch
import scipy.optimize as sciopt

import util

def main():
    x_0 = torch.tensor([1.3, 0.7, 0.8, 1.9, 1.2])
    print('x_0=', x_0)

    assert torch.allclose( util.rosenbrock(x_0), torch.tensor([sciopt.rosen(x_0.numpy())], dtype=torch.float32) )
    print('Test util.rosenbrock() vs scipy: OK')

    assert torch.allclose(util.grad(util.rosenbrock, x_0), torch.from_numpy(sciopt.rosen_der(x_0.numpy())), rtol=1e-03, atol=1e-03)
    print('Test util.grad() vs scipy: OK')

if __name__ == '__main__':
    main()
