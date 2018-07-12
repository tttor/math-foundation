import torch

import util
from algor_03_06_zoom import zoom

def line_search_algorithm(fn, x_k, p_k, alpha_max):
    '''
    \param
        alpha_max: bound on the maximum step length allowed; p60

    \return
        alpha_star: a step length that satisfies the strong Wolfe conditions; p60

    # notation map:
    * alpha: alpha_i
    * prev_alpha: alpha_{i-1}
    '''
    def phi(alpha):
        return fn(x_k + alpha * p_k) # equ 3.55, p56

    alpha = 1.0 # p59, speficifally for For Newton and quasi-Newton methods
    prev_alpha = 0.0

    # c1 and c2 satisfying 0 < c1 < c2 < 1; p60
    # c1 = 10^{-4} and c2 = 0.9; p62
    # c1 is usually chosen to be small in practice (c1 = 10-4 , say); p57
    c1 = 1e-4
    c2 = 0.9

    i = 1
    while True:
        phi_alpha = phi(alpha)
        phi_prev_alpha = phi(prev_alpha)
        phi_0 = phi(0.0)
        phi_der_0 = util.grad(phi, torch.zeros(1))

        if (phi_alpha > phi_0 + c1 * alpha * phi_der_0) or (phi_alpha >= phi_prev_alpha and i > 1):
            alpha_star = zoom(prev_alpha, alpha, phi, c1, c2)
            return alpha_star

        phi_der_alpha = util.grad(phi, torch.tensor([alpha]))

        if abs(phi_der_alpha) <= -c2 * phi_der_0:
            alpha_star = alpha
            return alpha_star

        if phi_der_alpha >= 0.0:
            alpha_star = zoom(alpha, prev_alpha, phi, c1, c2)
            return alpha_star

        prev_alpha = alpha
        alpha = uniformly_random(alpha, alpha_max)

        i += 1
