#!/usr/bin/env python3
import torch
from torch.autograd import Variable

def grad(fn, _x):
    # clone the input _x, so that we do not need to zero the gradients using x.grad.zero_()
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    out.backward()
    return x.grad

def hess_vec_prod(fn, _x, v):
    # https://discuss.pytorch.org/t/calculating-hessian-vector-product/11240
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    grad_f, = torch.autograd.grad(out, x, create_graph=True)
    z = torch.dot(grad_f, v)
    z.backward()
    assert torch.allclose(x.grad, torch.from_numpy(sciopt.rosen_hess_prod(x.detach().numpy(), v.double())), rtol=1e-03, atol=1e-03)
    return x.grad

def rosenbrock(x):
    # https://en.wikipedia.org/wiki/Rosenbrock_function
    # \param x: a 1D tensor, i.e a vector
    return sum( 100*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0 )
