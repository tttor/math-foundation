# ch06_quasi_newton_methods.md

* Quasi-Newton methods
  * like steepest descent,
    require **only the gradient** of the objective function to be supplied at each iterate.
  * By measuring the changes in gradients, they
    construct a model of the objective function that is good enough to
    produce superlinear convergence.

# 6.1 the bfgs method
* $B_k$ is an $n \times n$ symmetric positive definite matrix
  * that will be revised or updated at every iteration.
* the key difference with Newton method is that
  * the approximate Hessian Bk is used in place of the true Hessian.
* Davidon proposed
  * Instead of computing B k afresh at every iteration,
    * to update it in a
      simple manner to account for the curvature measured during the most recent step
  * One reasonable requirement is that the gradient of m k+1 should match the
    gradient of the objective function f at the latest two iterates xk and xk+1 .

## properties of the bfgs method
* BFGS: the superlinear rate of convergence

## implementation
* The line search, which should satisfy either the Wolfe conditions (3.6) or the strong Wolfe conditions (3.7),
  * should always try the step length $\alpha_k = 1$ first,
    * because this step length will eventually always be accepted (under certain conditions),
    * thereby producing superlinear convergence of the overall algorithm.
