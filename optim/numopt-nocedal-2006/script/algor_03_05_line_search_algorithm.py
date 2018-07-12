algor_03_05_line_search_algorithm.py

def main():
    pass

def line_search_algorithm():
    prev_alpha = 0
    alpha =
    alpha_max =

    c1 =
    c2 =

    i = 1
    while True:
        phi_alpha = phi(alpha)
        phi_prev_alpha = phi(prev_alpha)
        phi_0 = phi(0.0)
        phi_der_0 = phi_der(0.0)

        if (phi_alpha > phi_0 + c1 * alpha * phi_der_0)
            or (phi_alpha >= phi_prev_alpha and i > 1):
            return zoom(prev_alpha, alpha)

        phi_der_alpha = phi_der(alpha)

        if abs(phi_der_alpha) <= -c2 * phi_der_0:
            return alpha

        if phi_der_alpha >= 0.0:
            return zoom(alpha, prev_alpha)

        prev_alpha = alpha
        alpha =

        i += 1


def phi(alpha):
    pass

if __name__ == '__main__':
    main()
