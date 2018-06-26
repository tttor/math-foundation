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

### the wolfe conditions
* Armijo condition.
* curvature condition
* The sufficient decrease and curvature conditions are known collectively
  as the Wolfe conditions.
* strong Wolfe conditions
* The Wolfe conditions are scale-invariant in a broad sense:
  * Multiplying the objective function by a constant or
    making an affine change of variables does not alter them

### the goldstein conditions
TODO
