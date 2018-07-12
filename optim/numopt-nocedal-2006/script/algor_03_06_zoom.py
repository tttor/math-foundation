def zoom(alpha_lo, alpha_hi):
    while True:
        alpha_j = interpolate(alpha_lo, alpha_hi)

        phi_alpha_j = phi(alpha_j)
        phi_alpha_lo = phi(alpha_lo)

        if (phi_alpha_j > phi_0 + c1 * alpha_j * phi_der_0)
            or (phi_alpha_j >= phi_alpha_lo):
            alpha_hi = alpha_j
        else:
            phi_der_alpha_j = phi_der(alpha_j)
            phi_der_0 = phi_der(0.0)

            if abs(phi_der_alpha_j) <= -c2 * phi_der_0:
                return alpha_j

            if phi_der_alpha_j * (alpha_hi - alpha_lo) >= 0.0:
                alpha_hi = alpha_lo

            alpha_lo = alpha_j

def interpolate():
    pass
