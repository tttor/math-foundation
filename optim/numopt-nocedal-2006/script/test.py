#!/usr/bin/env python3
import torch
import scipy.optimize as sciopt

import util

def main():
    x = torch.tensor([1.3, 0.7, 0.8, 1.9, 1.2])
    print('x=', x)

    assert torch.allclose(util.rosenbrock(x),
                          torch.tensor([sciopt.rosen(x.numpy())], dtype=torch.float32))
    print('Test util.rosenbrock() vs scipy: OK')

    assert torch.allclose(util.grad(util.rosenbrock, x),
                          torch.from_numpy(sciopt.rosen_der(x.numpy())), rtol=1e-03, atol=1e-03)
    print('Test util.grad() vs scipy: OK')

    v = torch.rand_like(x)
    assert torch.allclose(util.hess_vec_prod(util.rosenbrock, x, v),
                          torch.from_numpy(sciopt.rosen_hess_prod(x.numpy(), v.numpy())), rtol=1e-03, atol=1e-03)
    print('Test util.hess_vec_prod() vs scipy: OK')

if __name__ == '__main__':
    main()
