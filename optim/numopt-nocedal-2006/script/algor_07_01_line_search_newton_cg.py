#!/usr/bin/env python3
# https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html

import torch
from torch.autograd import Variable

import numpy as np
import scipy.optimize as sciopt

def main():
    x_0 = torch.tensor([1.3, 0.7, 0.8, 1.9, 1.2])
    # assert np.allclose(rosen(x_0).numpy(), sciopt.rosen(x_0.numpy()))

    # test own implementation
    res = line_search_newton_cg(rosen, x_0, max_k_iter=15, max_j_iter=10)
    print('res= '+str(res))

    # # scipy opt
    # print('### scipy opt: Newton-CG...')
    # res_newtoncg = sciopt.minimize(rosen, x_0.numpy(), method='Newton-CG',
    #                               jac=sciopt.rosen_der, hessp=sciopt.rosen_hess_prod,
    #                               options={'xtol': 1e-8, 'disp': True})
    # print(res_newtoncg)

    # print('### scipy opt: L-BFGS-B...')
    # res_lbfgs = sciopt.minimize(rosen, x_0.numpy(), method='L-BFGS-B', jac=sciopt.rosen_der,
    #                             options={'disp': False})
    # print(res_lbfgs)

    # print('### scipy opt: CG...')
    # res_cg = sciopt.minimize(rosen, x_0.numpy(), method='CG', jac=sciopt.rosen_der,
    #                             options={'disp': False})
    # print(res_cg)

def line_search_newton_cg(fn, x_0, max_k_iter, max_j_iter):
    '''
    Algorithm 7.1 (Line Search Newton-CG)
    x_k: the solution that minimizes fn
    p_k: search step direction
    alpha_k: search step length
    eps_k:  a tolerance that specifies the required accuracy of the computed
    d: the search directions for inner CG iteration
    {z_j}: inner iteration sequence;
            when Bk is positive definite, the inner iteration sequence {z_j} will
            converge to the Newton step pk N that solves (7.9)
    jprime: j+1
    '''
    def grad(_x):
        # clone the input _x, so that we do not need to zero the gradients using x.grad.zero_()
        x = Variable(_x.data.clone(), requires_grad=True)
        out = fn(x)
        out.backward()
        assert np.allclose(x.grad.numpy(), sciopt.rosen_der(x.detach().numpy()), rtol=1e-03, atol=1e-03)
        return x.grad

    def hess_vec_prod(_x, v):
        # https://discuss.pytorch.org/t/calculating-hessian-vector-product/11240
        x = Variable(_x.data.clone(), requires_grad=True)
        out = fn(x)
        grad_f, = torch.autograd.grad(out, x, create_graph=True)
        z = torch.dot(grad_f, v)
        z.backward()
        assert np.allclose(x.grad.numpy(), sciopt.rosen_hess_prod(x.detach().numpy(), v.double()), rtol=1e-03, atol=1e-03)
        return x.grad

    # init the solution x_k
    x_k = x_0

    for k in range(max_k_iter):
        # get the search step direction, p_k, via CG
        eps_k = min( 0.5, torch.sqrt(torch.norm(grad(x_k))) ) * torch.norm(grad(x_k))
        z_j = Variable(torch.zeros_like(x_k))
        r_j = grad(x_k)
        d_j = -r_j

        for j in range(max_j_iter):
            if torch.dot(d_j, hess_vec_prod(x_k, d_j)) <= 0.0:# the negative curvature test
                if j == 0:
                    p_k = -grad(x_k)
                else:
                    p_k = z_j

                break

            alpha_j = torch.dot(r_j, r_j) / torch.dot(d_j, hess_vec_prod(x_k, d_j))

            z_jprime = z_j + alpha_j * d_j
            r_jprime = r_j + alpha_j * hess_vec_prod(x_k, d_j)

            if torch.norm(r_j) < eps_k:
                p_k = z_jprime

                z_j = z_jprime
                r_j = r_jprime
                break

            beta_jprime = torch.dot(r_jprime, r_jprime) / torch.dot(r_j, r_j)
            d_jprime = -r_jprime + beta_jprime*d_j

            z_j = z_jprime
            r_j = r_jprime
            d_j = d_jprime

        # get the search step length, alpha_k
        # that satisfies the Wolfe, Goldstein, or Armijo backtracking conditions
        alpha_k = 1.0

        # update x_k
        x_kprime = torch.add(x_k, alpha_k * p_k)
        x_k = x_kprime

    return x_k

def rosen(x):
    # The Rosenbrock function
    # \param x: a 1D tensor, i.e a vector
    return sum( 100*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0 )

if __name__ == '__main__':
    main()
