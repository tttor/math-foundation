# ch03: Line Search Methods

* Each iteration of a line search method
  * computes a search direction $p_k$ and
  * then decides how far to move along that direction.
* the iteration: $x_{k+1} = x_k + \alpha_k p_k$
  * $\alpha_k$: step length
* the search direction has the form: $p_k = - B_k^{-1} \nabla f_k$
  *  $B_k$ is a symmetric and nonsingular matrix.
  * steepest descent: $B_k$ is the identity matrix
  * Newton's method:  $B_k$ is the exact Hessian $\nabla^2 f(x_k)$
  * quasi-Newton methods: $B_k$ is an approximation to the Hessian that
    is updated at every iteration by means of a low-rank formula

## 3.1 step length
* a tradeoff.
  * to choose $\alpha_k$ to give a substantial reduction of f
  * but at the same time we do not want to spend too much time making the choice
* ensure that the step length α achieves sufficient decrease but is not too short.

### the wolfe conditions
* Armijo condition.
* curvature condition
* the sufficient decrease and curvature conditions are known collectively
  as the wolfe conditions.
* strong wolfe conditions
* the wolfe conditions are scale-invariant in a broad sense:
  * multiplying the objective function by a constant or
    making an affine change of variables does not alter them

### the goldstein conditions
* often used in Newton-type methods
  * but are not well suited for quasi-Newton methods that
    maintain a positive definite Hessian approximation.

### sufficient decrease and backtracking
* Backtracking Line Search

## 3.2 convergence of line search methods
TODO

## 3.3 rate of convergence
### newton’s method
* the search is given by
  * $p_k^N = - \nabla^2 f_k^{-1} \nabla f_k$

### quasi-newton methods
* search direction has the form
  * $p_k = - B_k^{-1} \nabla f_k$

## 3.4 newton’s method with hessian modification
* Line Search Newton with Modification

## 3.5 step-length selection algorithms
TODO
