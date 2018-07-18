#!/usr/bin/env python3
import torch

import util
from algor_03_05_line_search_algorithm import line_search_algorithm

def line_search_newton_cg(fn, x_0, max_k_iter, max_j_iter):
    '''
    Algorithm 7.1 (Line Search Newton-CG), p169

    \notation
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
    x_k = x_0 # init the solution x_k

    for k in range(max_k_iter):
        # get the search step direction, p_k, via CG
        grad_x_k = util.grad(fn, x_k)
        eps_k = min( 0.5, torch.sqrt(torch.norm(grad_x_k)) ) * torch.norm(grad_x_k)
        z_j = torch.zeros_like(x_k)
        r_j = grad_x_k
        d_j = -r_j

        for j in range(max_j_iter):
            hvp_xk_dj = util.hess_vec_prod(fn, x_k, d_j)

            if torch.dot(d_j, hvp_xk_dj) <= 0.0:# the negative curvature test, p170
                if j == 0:
                    p_k = -grad_x_k
                else:
                    p_k = z_j

                break

            alpha_j = torch.dot(r_j, r_j) / torch.dot(d_j, hvp_xk_dj)

            z_jprime = z_j + alpha_j * d_j
            r_jprime = r_j + alpha_j * hvp_xk_dj

            if torch.norm(r_j) < eps_k:
                p_k = z_jprime

                z_j = z_jprime
                r_j = r_jprime
                break

            beta_jprime = torch.dot(r_jprime, r_jprime) / torch.dot(r_j, r_j)
            d_jprime = -r_jprime + (beta_jprime * d_j)

            z_j = z_jprime
            r_j = r_jprime
            d_j = d_jprime

        # get the search step length, alpha_k
        # that satisfies the Wolfe, Goldstein, or Armijo backtracking conditions
        # (using alpha_k = 1 if possible)
        alpha_k = line_search_algorithm(fn, x_k, p_k, alpha_max=1.0)

        # update x_k
        x_kprime = torch.add(x_k, alpha_k * p_k)
        x_k = x_kprime

    return x_k
