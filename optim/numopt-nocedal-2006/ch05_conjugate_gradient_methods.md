# ch05_conjugate_gradient_methods.md

* interest in conjugate gradient methods is twofold.
  * they are among the most useful techniques for solving large linear systems of equations.
  * they can be adapted to solve nonlinear optimization problems.

## 5.1 the linear conjugate gradient method
* The CG method is recommended only for large problems;
  * otherwise, Gaussian elimination or other factorization algorithms such as
    the singular value decomposition are to be preferred,
    since they are less sensitive to rounding errors.
* For large problems, the CG method has the advantage that
  * it does not alter the coefficient matrix and
  * (in contrast to factorization techniques) does not produce fill in the arrays holding the matrix.
  * CG method sometimes approaches the solution quickly,

## 5.2 nonlinear conjugate gradient methods
TODO
