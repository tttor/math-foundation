#!/usr/bin/env python3
import torch
import scipy.optimize as sciopt

import util
from algor_07_01_line_search_newton_cg import line_search_newton_cg

def main():
    torch.manual_seed(12345)

    x = torch.tensor([1.3, 0.7, 0.8, 1.9, 1.2])
    print('x=', x)
    # test_util(x)

    # Test
    # algor_03_05_line_search_algorithm.py
    # algor_03_06_zoom.py
    # algor_07_01_line_search_newton_cg.py
    res = line_search_newton_cg(util.rosenbrock, x_0=x, max_k_iter=15, max_j_iter=10)
    print('line_search_newton_cg=', res)

    res_scipy = sciopt.minimize(sciopt.rosen, x.numpy(), method='Newton-CG',
                                jac=sciopt.rosen_der, hessp=sciopt.rosen_hess_prod)
    assert torch.allclose(res, torch.from_numpy(res_scipy.x), rtol=1e-03, atol=1e-03)

def test_util(x):
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
