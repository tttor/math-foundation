# ch06_quasi_newton_methods.md

* Quasi-Newton methods, like steepest descent,
  * require only the gradient of the objective function to be supplied at each iterate.
  * By measuring the changes in gradients, they
    construct a model of the objective function that is good enough to produce superlinear
    convergence.

## 6.1 the bfgs method
* $B_k$ is an $n \times n$ symmetric positive definite matrix
  * that will be revised or updated at every iteration.

### properties of the bfgs method
* BFGS: the superlinear rate of convergence

### implementation
* The line search, which should satisfy either the Wolfe conditions (3.6) or the strong Wolfe conditions (3.7), 
  * should always try the step length $\alpha_k = 1$ first,
    * because this step length will eventually always be accepted (under certain conditions), 
    * thereby producing superlinear convergence of the overall algorithm.
