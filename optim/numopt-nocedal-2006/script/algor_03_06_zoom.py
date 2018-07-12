#!/usr/bin/env python3
import math

import torch

import util

def zoom(alpha, prev_alpha, phi, c1, c2):
    '''
    Algorithm 3.6 (zoom), p61
    '''
    while True:
        alpha_j = cubic_interpolation(alpha, prev_alpha, phi)

        phi_alpha_j = phi(alpha_j)

        if alpha > prev_alpha:
            alpha_hi = alpha
            alpha_lo = prev_alpha
        else:
            alpha_hi = prev_alpha
            alpha_lo = alpha

        phi_alpha_lo = phi(alpha_lo)
        phi_0 = phi(0.0)
        phi_der_0 = util.grad(phi, torch.zeros(1))

        if (phi_alpha_j > (phi_0 + c1 * alpha_j * phi_der_0)) or (phi_alpha_j >= phi_alpha_lo):
            alpha_hi = alpha_j
        else:
            phi_der_alpha_j = util.grad(phi, torch.tensor([alpha_j]))

            if abs(phi_der_alpha_j) <= (-c2 * phi_der_0):
                return alpha_j

            if (phi_der_alpha_j * (alpha_hi - alpha_lo)) >= 0.0:
                alpha_hi = alpha_lo

            alpha_lo = alpha_j

def cubic_interpolation(alpha, prev_alpha, phi):
    '''
    refer to equ 3.59, p59
    '''
    phi_alpha = phi(alpha)
    phi_prev_alpha = phi(prev_alpha)
    phi_der_alpha = util.grad(phi, torch.tensor([alpha]))
    phi_der_prev_alpha = util.grad(phi, torch.tensor([prev_alpha]))

    sign = lambda x: math.copysign(1, x) # https://stackoverflow.com/questions/1986152/why-doesnt-python-have-a-sign-function

    d1 = phi_der_prev_alpha + phi_der_alpha - 3 * ( (phi_prev_alpha - phi_alpha) / (prev_alpha - alpha) )
    d2 = sign(alpha - prev_alpha) * math.sqrt(d1**2 - phi_der_prev_alpha * phi_der_alpha )

    next_alpha = alpha - (alpha - prev_alpha) * ( (phi_der_alpha + d2 - d1) / (phi_der_alpha - phi_der_prev_alpha + 2*d2) )
    return next_alpha
