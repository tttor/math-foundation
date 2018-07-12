import torch

import util

def zoom(alpha_lo, alpha_hi, phi, c1, c2):
    while True:
        alpha_j = interpolate(alpha_lo, alpha_hi)

        phi_alpha_j = phi(alpha_j)
        phi_alpha_lo = phi(alpha_lo)
        phi_0 = phi(0.0)
        phi_der_0 = util.grad(phi, torch.zeros(1))

        if (phi_alpha_j > phi_0 + c1 * alpha_j * phi_der_0) or (phi_alpha_j >= phi_alpha_lo):
            alpha_hi = alpha_j
        else:
            phi_der_alpha_j = util.grad(phi, torch.tensor([alpha_j]))

            if abs(phi_der_alpha_j) <= -c2 * phi_der_0:
                return alpha_j

            if phi_der_alpha_j * (alpha_hi - alpha_lo) >= 0.0:
                alpha_hi = alpha_lo

            alpha_lo = alpha_j

def interpolate(alpha_lo, alpha_hi):
    return util.uniformly_random(alpha_lo, alpha_hi)
