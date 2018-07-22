#!/usr/bin/env python3
import torch
from torch.autograd import Variable

def grad(fn, _x):
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    grad, = torch.autograd.grad(out, x, create_graph=False)
    return grad

def hess_vec_prod(fn, _x, v):
    # https://discuss.pytorch.org/t/calculating-hessian-vector-product/11240
    x = Variable(_x.data.clone(), requires_grad=True)
    out = fn(x)
    grad, = torch.autograd.grad(out, x, create_graph=True)
    prod = torch.dot(grad, v)
    grad, = torch.autograd.grad(prod, x, create_graph=True)
    return grad

def rosenbrock(x):
    # https://en.wikipedia.org/wiki/Rosenbrock_function
    # \param x: a 1D tensor, i.e a vector
    return sum( 100*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0 )

def uniformly_random(_lo, _hi):
    # https://stackoverflow.com/questions/44328530/how-to-get-a-uniform-distribution-in-a-range-r1-r2-in-pytorch
    eps = 1e-8
    lo = _lo + eps # to exclude _lo
    hi = _hi - eps # to exlude _hi
    rnd = (hi - lo) * torch.rand(1) + lo
    return rnd.item()
