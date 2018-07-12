#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Rosenbrock_function
# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.rosen.html

import torch
from torch.autograd import Variable

import scipy.optimize as sciopt

def rosen(x):
    # The Rosenbrock function
    # \param x: a 1D tensor, i.e a vector
    return sum( 100*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0 )

def rosen_grad(_x):
    # clone the input _x, so that we do not need to zero the gradients using x.grad.zero_()
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    out.backward()
    return x.grad

def rosen_hess_vec_prod(_x, v):
    # https://discuss.pytorch.org/t/calculating-hessian-vector-product/11240
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    grad_f, = torch.autograd.grad(out, x, create_graph=True)
    z = torch.dot(grad_f, v)
    z.backward()
    assert torch.allclose(x.grad, torch.from_numpy(sciopt.rosen_hess_prod(x.detach().numpy(), v.double())), rtol=1e-03, atol=1e-03)
    return x.grad

def test():
    x_0 = torch.tensor([1.3, 0.7, 0.8, 1.9, 1.2])
    print('x_0=', x_0)

    assert torch.allclose( rosen(x_0), torch.tensor([sciopt.rosen(x_0.numpy())], dtype=torch.float32) )
    print('Test rosen() vs scipy: OK')

    # assert torch.allclose(rosen_grad(x_0), torch.from_numpy(sciopt.rosen_der(x.detach().numpy())), rtol=1e-03, atol=1e-03)
    # print('Test rosen_grad() vs scipy: OK')

if __name__ == '__main__':
    test()
